from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from . import forms
from .models import User_details
from .models import user_requests
from .models import Team_details
from django.core.exceptions import ObjectDoesNotExist


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                temp = User_details.objects.get(user_user=user)
                request.session['gamer_data_verified'] = temp.data_verified
                request.session['gamer_authority'] = temp.authority
            except ObjectDoesNotExist:
                pass
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else :
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Project_Allotment_Portal:home')


def user_profile(request):
    update(request)
    if request.method == 'POST':
        form = forms.ProfileDetails(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user_user = request.user
            temp.data_verified = 1
            temp.save()
            return redirect('Project_Allotment_Portal:home')
    else:
        form = forms.ProfileDetails()

    return render(request, 'accounts/profile.html', {'form':form} )


def team(request):

    update(request)

    if request.method == 'POST':
        data = request.POST.copy()
        reg = data.get('reg')
        req = user_requests()
        req.user_from = request.user
        req.user_to = User_details.objects.get(user_reg_no = reg ).user_user
        req.save()

    mem1 = User_details.objects.filter(authority=1).filter(data_verified=2)
    mem2 = User_details.objects.filter(authority=2).filter(data_verified=2)
    mem3 = User_details.objects.filter(authority=3).filter(data_verified=2)
    mem4 = User_details.objects.filter(authority=4).filter(data_verified=2)
    mem5 = user_requests.objects.filter(user_from=request.user)
    mem1_ = User_details.objects.none()
    mem2_ = User_details.objects.none()
    mem3_ = User_details.objects.none()
    mem4_ = User_details.objects.none()

    mem6 = User_details.objects.none()

    for j in mem1:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                f=1
                break
        if f==0:
            mem1_ |= User_details.objects.filter(user_user = j.user_user)

    for j in mem2:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                # mem1.exclude(user_user = i.user_user )
                f=1
                break
        if f==0:
            mem2_ |= User_details.objects.filter(user_user = j.user_user)

    for j in mem3:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                # mem1.exclude(user_user = i.user_user )
                f=1
                break
        if f==0:
            mem3_ |= User_details.objects.filter(user_user = j.user_user)

    for j in mem4:
        f=0
        for i in mem5 :
            if j.user_user == i.user_to:
                # mem1.exclude(user_user = i.user_user )
                f=1
                break
        if f==0:
            mem4_ |= User_details.objects.filter(user_user = j.user_user)

    if request.session['gamer_authority'] == 1:
        tm = Team_details.objects.get(team_member_1=request.user)
        pass
    elif request.session['gamer_authority'] == 2:
        tm = Team_details.objects.get(team_member_2=request.user)
        pass
    elif request.session['gamer_authority'] == 3:
        tm = Team_details.objects.get(team_member_3=request.user)
        pass
    elif request.session['gamer_authority'] == 4:
        tm = Team_details.objects.get(team_leader=request.user)
        pass

    mem6 |= User_details.objects.filter(user_user=team_leader)
    mem6 |= User_details.objects.filter(user_user=team_member_3)
    mem6 |= User_details.objects.filter(user_user=team_member_2)
    mem6 |= User_details.objects.filter(user_user=team_member_1)

    return render(request, 'accounts/team.html', {'mem1':mem1_, 'mem2':mem2_, 'mem3':mem3_, 'mem4':mem4_, 'mem5':mem5 , 'mem6':mem6} )


def validate(request):
    update(request)
    return render(request, 'accounts/validate.html')


def requests(request):
    update(request)

    if request.method == 'POST':
        data = request.POST.copy()
        reg = data.get('reg')
        person = User_details.objects.get(user_reg_no=reg)

        if request.session['gamer_authority'] == 4 :

            team = Team_details.objects.get(team_leader=request.user)
            if person.authority == 1 :
                team.team_member_1 = person.user_user
                temp = User_details.objects.filter(authority=1)
                for i in temp :
                    user_requests.objects.filter(user_from=request.user).filter(user_to=i.user_user).delete()
                    user_requests.objects.filter(user_from=i.user_user).filter(user_to=request.user).delete()

            elif person.authority == 2 :
                team.team_member_2 = person.user_user
                temp = User_details.objects.filter(authority=2)
                for i in temp:
                    user_requests.objects.filter(user_from=request.user).filter(user_to=i.user_user).delete()
                    user_requests.objects.filter(user_from=i.user_user).filter(user_to=request.user).delete()

            elif person.authority == 3 :
                team.team_member_3 = person.user_user
                temp = User_details.objects.filter(authority=3)
                for i in temp:
                    user_requests.objects.filter(user_from=request.user).filter(user_to=i.user_user).delete()
                    user_requests.objects.filter(user_from=i.user_user).filter(user_to=request.user).delete()

            team.save()

            if team.team_member_1 != None and team.team_member_2 != None and team.team_member_3 != None :
                x=User_details.objects.get(user_user=request.user)
                x.data_verified=3
                x.save()

            user_requests.objects.filter(user_from=person.user_user).delete()
            user_requests.objects.filter(user_to=person.user_user).delete()

            person.data_verified=3
            person.save()

        else :

            team = Team_details.objects.get(team_leader=person.user_user)

            if request.session['gamer_authority'] == 1:
                team.team_member_1 = request.user
                temp = User_details.objects.filter(authority=1)
                for i in temp:
                    user_requests.objects.filter(user_from=person.user_user).filter(user_to=i.user_user).delete()
                    user_requests.objects.filter(user_from=i.user_user).filter(user_to=person.user_user).delete()

            elif request.session['gamer_authority'] == 2:
                team.team_member_2 = request.user
                temp = User_details.objects.filter(authority=1)
                for i in temp:
                    user_requests.objects.filter(user_from=person.user_user).filter(user_to=i.user_user).delete()
                    user_requests.objects.filter(user_from=i.user_user).filter(user_to=person.user_user).delete()

            elif request.session['gamer_authority'] == 3:
                team.team_member_3 = request.user
                temp = User_details.objects.filter(authority=1)
                for i in temp:
                    user_requests.objects.filter(user_from=person.user_user).filter(user_to=i.user_user).delete()
                    user_requests.objects.filter(user_from=i.user_user).filter(user_to=person.user_user).delete()

            team.save()

            #   Now team is updated and do rest all tasks

            x = Team_details.objects.filter(user_user=request.user)
            x.data_verified = 3
            x.save()

            if team.team_member_1 != None and team.team_member_2 != None and team.team_member_3 != None:
                person.data_verified = 3
                person.save()

            user_requests.objects.filter(user_from=request.user).delete()
            user_requests.objects.filter(user_to=request.user).delete()




    mem4 = User_details.objects.none()
    mem6 = User_details.objects.none()

    req = user_requests.objects.filter(user_to=request.user)

    for i in req :
        mem4 |= User_details.objects.filter(user_user = i.user_from)


    if request.session['gamer_authority'] == 1 :
        tm = Team_details.objects.get(team_member_1=request.user)
        pass
    elif request.session['gamer_authority'] == 2 :
        tm = Team_details.objects.get(team_member_2=request.user)
        pass
    elif request.session['gamer_authority'] == 3 :
        tm = Team_details.objects.get(team_member_3=request.user)
        pass
    elif request.session['gamer_authority'] ==4 :
        tm = Team_details.objects.get(team_leader=request.user)
        pass

    mem6 |= User_details.objects.filter(user_user=team_leader)
    mem6 |= User_details.objects.filter(user_user=team_member_3)
    mem6 |= User_details.objects.filter(user_user=team_member_2)
    mem6 |= User_details.objects.filter(user_user=team_member_1)

    return render(request, 'accounts/requests.html',{'mem4':mem4,'mem6':mem6})


def update(request):
    try:
        if request.user.is_authenticated:
            temp = User_details.objects.get(user_user=request.user)
            request.session['gamer_data_verified'] = temp.data_verified
            request.session['gamer_authority'] = temp.authority
        else :
            request.session['gamer_data_verified'] = 0
            request.session['gamer_authority'] = 0
    except ObjectDoesNotExist:
        request.session['gamer_data_verified'] = 0
        request.session['gamer_authority'] = 0


