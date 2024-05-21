# -*- coding: utf-8 -*-
"""

Created on Mon May  6 15:47:35 2024

@author: IAN CARTER KULANI
Phone:+265(0)988061969
E-mail:iancarterkulani@gmail.com
Purpose:The software prompts the user to enter total number of published centers,total 
number of registered  voters, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes 
and displays the results on the screen.
#NOTE:For a candidate to be a majority winner of an election, the candidate total valid votes should 
be greater than majority votes, which is Fifty plus one. 

"""


print("=========================================SOUTH AFRICA 2009 PRESIDENTIAL ELECTION=========================================\n\n")

percent=100
#Get total number of published center
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))


#Get Total Valid Votes
Totalvalidvotes=int(input("Enter Total Valid Votes:"))


#Get Total Vald Votes for African National Congress
Totalvalidvotesfor_African_National_Congress=int(input("Enter Total Valid Votes for African National Congress:"))


#Get Total Vald Votes for Democratic Alliance
Totalvalidvotesfor_Democratic_Alliance=int(input("Enter Total Valid Votes for Democratic Alliance:"))
#Get Total Vald Votes for Congress of the People
Totalvalidvotesfor_Congress_of_the_People=int(input("Enter Total Valid Votes for Congress of the People:"))
#Get Total Valid Votes for Inkatha Freedom Party  
Totalvalidvotesfor_Inkatha_Freedom_Party=int(input("Enter Total Valid Votes for Inkatha Freedom Party:"))
#Get Total Valid Votes for Independent Democrats
Totalvalidvotesfor_Independent_Democrats=int(input("Enter Total Valid Votes for Independent Democrats:"))
#Get TotalValid Votes for United Democratic Movement
Totalvalidvotesfor_United_Democratic_Movement=int(input("Enter Total Valid Votes for United Democratic Movement:"))
#Get Total Vald Votes for Freedom Front Plus
Totalvalidvotesfor_Freedom_Front_Plus=int(input("Enter Total Valid Votes for Freedom Front Plus:"))
#Get Total Vald Votes for African Christian Democratic Party
Totalvalidvotesfor_African_Christian_Democratic_Party=int(input("Enter Total Valid Votes for African Christian Democratic Party:"))
#Get Total Vald Votes for United Christian Democratic Party
Totalvalidvotesfor_United_Christian_Democratic_Party=int(input("Enter Total Valid Votes for United Christian Democratic Party:"))
#Get Total Vald Votes for Pan Africanist Congress
Totalvalidvotesfor_Pan_Africanist_Congress=int(input("Enter Total Valid Votes for Pan Africanist Congress:"))
#Get Total Vald Votes for Minolity Front
Totalvalidvotesfor_Minolity_Front=int(input("Enter Total Valid Votes for Minolity Front:"))
#Get Total Vald Votes for Azanian People's Organisation
Totalvalidvotesfor_Azanian_Peoples_Organisation=int(input("Enter Total Valid Votes for Azanian People's Organisation:"))
#Get Total Valid Votes for African People's Convention
Totalvalidvotesfor_African_Peoples_Convention=int(input("Enter Total Valid Votes for African People's Convention:"))
#Get Total Valid Votes for Movement Democratic Party
Totalvalidvotesfor_Movement_Democratic_Party=int(input("Enter Total Valid Votes for Movement Democratic Party:"))
#Get Total Valid Votes for Al Jamal-Ah
Totalvalidvotesfor_Al_Jamal_Ah=int(input("Enter Total Valid Votes for Al Jamal-Ah:"))
#Get Total Vald Votes for Christian Democratic Alliance
Totalvalidvotesfor_Christian_Democratic_Alliance=int(input("Enter Total Valid Votes for Christian Democratic Alliance:"))
#Get Total Valid Votes for National Democratic Convention
Totalvalidvotesfor_National_Democratic_Convention=int(input("Enter Total Valid Votes for National Democratic Convention:"))
#Get Total Valid Votes for New Vision Party
Totalvalidvotesfor_New_Vision_Party=int(input("Enter Total Valid Votes for New Vision Party:"))
#Get Total Valid Votes for United Independent Front
Totalvalidvotesfor_United_Independent_Front=int(input("Enter Total Valid Votes for United Independent Front:"))
#Get Total Valid Votes for Great Kongress of South Africa
Totalvalidvotesfor_Great_Kongress_of_South_Africa=int(input("Enter Total Valid Votes for Great Kongress of South Africa:"))
#Get Total Vald Votes for South Africa Democratic Congress
Totalvalidvotesfor_South_Africa_Democratic_Congress=int(input("Enter Total Valid Votes for South Africa Democratic Congress:"))
#Get Total Vald Votes for Keep it Straight and Simple Party
Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party=int(input("Enter Total Valid Votes for Keep it Straight and Simple Party:"))
#Get Total Vald Votes for Pan Africanist Movement
Totalvalidvotesfor_Pan_Africanist_Movement=int(input("Enter Total Valid Votes for Pan Africanist Movement:"))
#Get Total Vald Votes for Alliance for Free Democrats
Totalvalidvotesfor_Alliance_for_Free_Democrats=int(input("Enter Total Valid Votes for Alliance for Free Democrats:"))
#Get Total Vald Votes for Women Foward
Totalvalidvotesfor_Women_Foward=int(input("Enter Total Valid Votes for Women Foward:"))

#Get Total Vald Votes for A Party
Totalvalidvotesfor_A_Party=int(input("Enter Total Valid Votes for A Party:"))

#Decision Making

if Totalvalidvotesfor_African_National_Congress>Totalvalidvotes/2+1 :
     print("Congratulations to the African National Congress For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Democratic_Alliance>Totalvalidvotes/2+1: 
     print("Congratulations to the Democratic Alliance For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Inkatha_Freedom_Party>Totalvalidvotes/2+1:
     print("Congratulations to the Inkatha Freedom Party For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Independent_Democrats>Totalvalidvotes/2+1: 
     print("Congratulations to the Independent Democrats For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_United_Democratic_Movement>Totalvalidvotes/2+1: 
     print("Congratulations to the United Democratic Movement For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Freedom_Front_Plus>Totalvalidvotes/2+1 :
     print("Congratulations to the Freedom Front Plus For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_African_Christian_Democratic_Party>Totalvalidvotes/2+1: 
     print("Congratulations to the African Christian Democratic Party For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Pan_Africanist_Congress>Totalvalidvotes/2+1: 
     print("Congratulations to the Pan Africanist Congress For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Minolity_Front>Totalvalidvotes/2+1 :
     print("Congratulations to the Minolity Front For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Azanian_Peoples_Organisation>Totalvalidvotes/2+1: 
     print("Congratulations to theAzanian Peoples Organisation For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_African_Peoples_Convention>Totalvalidvotes/2+1: 
     print("Congratulations to the Socialist Revolutionary African People's Convention For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Movement_Democratic_Party>Totalvalidvotes/2+1: 
     print("Congratulations to the Movement Democratic Party For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Al_Jamal_Ah>Totalvalidvotes/2+1: 
     print("Congratulations to the Al Jamal Ah For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Christian_Democratic_Alliance>Totalvalidvotes/2+1 :
     print("Congratulations to the Christian_Democratic_Alliance Party For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_National_Democratic_Convention>Totalvalidvotes/2+1: 
     print("Congratulations to the National Democratic ConventionFor Winning 2009 Election\n\n")
elif Totalvalidvotesfor_United_Independent_Front>Totalvalidvotes/2+1: 
     print("Congratulations to theUnited Independent Front For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Great_Kongress_of_South_Africa>Totalvalidvotes/2+1:
     print("Congratulations to the Great Kongress of South Africa For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_South_Africa_Democratic_Congress>Totalvalidvotes/2+1: 
     print("Congratulations to theSouth Africa Democratic Congress For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party>Totalvalidvotes/2+1: 
     print("Congratulations to the Keep it Straight and Simple Party For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Pan_Africanist_Movement>Totalvalidvotes/2+1 :
     print("Congratulations to the Pan Africanist Movement For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Alliance_for_Free_Democrats>Totalvalidvotes/2+1: 
     print("Congratulations to the Alliance for  Free Democrats For Winning 2009 Election\n\n")
elif Totalvalidvotesfor_Women_Foward>Totalvalidvotes/2+1: 
     print("Congratulations to the Women Foward For Winning 2009 Election\\n\n")
elif Totalvalidvotesfor_A_Party>Totalvalidvotes/2+1:  
     print("Congratulations to A Party For Winning 2009 Election\\n\n")

else:
    print("No majority winner was found RUNOFF may be required\n")
    

print("__________________________________________________________ELECTION STATISTICS__________________________________________________________\n")
#calculating percentage 
#Calculating percentage for total votes cast
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#Calculating percentage for Total Registered voters/turnout
Percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for African National Congress
Percentage=round(Totalvalidvotesfor_African_National_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African National Congress in Percentage=",Percentage)
#Calculating percentage for Democratic Alliance
Percentage=round(Totalvalidvotesfor_Democratic_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Democratic Alliance in percentage=",Percentage) 
#Calculating percentage for Inkatha Freedom Party
Percentage=round(Totalvalidvotesfor_Inkatha_Freedom_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Inkatha Freedom Party in percentage=",Percentage) 
#Calculating percentage for Independent Democrats
Percentage=round(Totalvalidvotesfor_Independent_Democrats*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Independent Democrats in Percentage=",Percentage)
#Calculating percentage for United Democratic Movement
Percentage=round(Totalvalidvotesfor_United_Democratic_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Democratic Movement in percentage=",Percentage)
#Calculating percentage for Freedom Front Plus
Percentage=round(Totalvalidvotesfor_Freedom_Front_Plus*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Freedom Front Plus in percentage=",Percentage)  
#Calculating percentage for African Christian Democratic Party
Percentage=round(Totalvalidvotesfor_African_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Christian Democratic Party in percentage=",Percentage) 
#Calculating percentage for Pan Africanist Congress
Percentage=round(Totalvalidvotesfor_Pan_Africanist_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan Africanist Congress in Percentage=",Percentage)
#Calculating percentage for United Democratic Movement
Percentage=round(Totalvalidvotesfor_United_Democratic_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Democratic Movement in percentage=",Percentage)
#Calculating percentage for Pan Africanist Congress
Percentage=round(Totalvalidvotesfor_Pan_Africanist_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan Africanist Congress in percentage=",Percentage)  
#Calculating percentage for Minolity Front
Percentage=round(Totalvalidvotesfor_Minolity_Front*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Minolity Front in percentage=",Percentage)  
#Calculating percentage for Azanian Peoples Organisation
Percentage=round(Totalvalidvotesfor_Azanian_Peoples_Organisation*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Azanian Peoples Organisation in Percentage=",Percentage)
#Calculating percentage for African Peoples Convention
Percentage=round(Totalvalidvotesfor_African_Peoples_Convention*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Peoples Convention in percentage=",Percentage)
#Calculating percentage for Movement Democratic Party
Percentage=round(Totalvalidvotesfor_Movement_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Movement Democratic Party in percentage=",Percentage) 
#Calculating percentage for Al_Jamal Ah
Percentage=round(Totalvalidvotesfor_Al_Jamal_Ah*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Al_Jamal-Ah in percentage=",Percentage)  
#Calculating percentage for Christian Democratic Alliance
Percentage=round(Totalvalidvotesfor_Christian_Democratic_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Christian Democratic Alliance in percentage=",Percentage)
#Calculating percentage for National Democratic Convention
Percentage=round(Totalvalidvotesfor_National_Democratic_Convention*percent/Totalvalidvotes, 2);
print("Total Valid Votes for National Democratic Convention in percentage=",Percentage) 
#Calculating percentage for Great Kongress of South Africa
Percentage=round(Totalvalidvotesfor_Great_Kongress_of_South_Africa*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Great Kongress of South Africa in percentage=",Percentage)  
#Calculating percentage for South Africa Democratic Congress
Percentage=round(Totalvalidvotesfor_South_Africa_Democratic_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for South Africa Democratic Congress in Percentage=",Percentage)
#Calculating percentage for Keep it Straight and Simple Party
Percentage=round(Totalvalidvotesfor_Keep_it_Straight_and_Simple_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Keep it Straight and Simple Party in percentage=",Percentage)
#Calculating percentage for Pan Africanist Movement
Percentage=round(Totalvalidvotesfor_Pan_Africanist_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan Africanist Movement in percentage=",Percentage)  
#Calculating percentage for Free Democrats
Percentage=round(Totalvalidvotesfor_Alliance_for_Free_Democrats*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Alliance for Free Democrats in percentage=",Percentage) 
#Calculating percentage for African Women Foward
Percentage=round(Totalvalidvotesfor_Women_Foward*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Women Foward in percentage=",Percentage)
#Calculating percentage for A Party
Percentage=round(Totalvalidvotesfor_A_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for A Party in percentage=",Percentage)


print("=========================================================================================================================\n")