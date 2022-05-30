# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:11:16 2021

@author: ali_d
"""
import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        
class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn =False
        self.currentUser = {}
        
        #load users from .json file
        self.loadUsers()
        
    
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users =json.load(file)
                #print(users)
                for user in users:
                    user = json.loads(user)
                    #print(user["username"])
                    newUser = User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users)
    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("kullanıcı oluşturuldu.")
        
    
    def logain(self,username,password):
        # if self.isLoggedIn:
        #     print("zaten logain oldunuz")
        # else:  
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedIn = True
                self.currentUser = user
                print("login yapıldı")
                break
            
        
        
    def logout(self):
        self.isLoggedIn=False
        self.currentUser = {}
        print("Çıkış yapıldı.")
        
    def identiy(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("giriş yapılmadı")
        
    
    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open("users.json","w") as file:
            json.dump(list,file)
            
            

repository = UserRepository()
    
    
while True:
    print("menü".center(50,"*"))
    secim = input("1-Register\n2-Logain\n3-Logout\n4-identiy\n5-Exit\nseçiminiz: ")
    if secim == "5":
        break
    else:
        if secim =="1":#register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            
            user = User(username=username, password=password, email=email)
            repository.register(user)
            
            #print(repository.users)
            
        elif secim =="2":
            if repository.isLoggedIn:
                print("zaten kayıt oldunuz")
            else:
                username = input("username: ")
                password = input("password: ")
            
                repository.logain(username, password)
        elif secim =="3":#logput
            repository.logout()
        elif secim =="4":#display username
            repository.identiy()
        else:
            print("yanlıs secim")
        
        
        













































































