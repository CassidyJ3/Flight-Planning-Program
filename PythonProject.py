#!/usr/bin/python3
# Program2.py
# Author: Joe Cassidy
# Purpose: To predict the best time to schedule a flight to Florida
# Date: 20 March, 2019
# Class: CSCI 431

from __future__ import print_function
import csv
import tkinter as flightProgram
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import *

#Checks if row is valid
def validateRow(Scheduled, Seats):
    if Scheduled > 0 and Seats > 0:
        return True
    else:
        return False

#Gives a column header from the string used in the combobox
def translate(cond):
    if cond == "Month":
        return "MONTH"
    if cond == "Origin City":
        return "ORIGIN_CITY_NAME"
    if cond == "Destination City":
        return "DEST_CITY_NAME"
    if cond == "Carrier":
        return "UNIQUE_CARRIER_NAME"
    if cond == "Aircraft":
        return "AIRCRAFT_TYPE"
    if cond == "Origin State":
        return "ORIGIN_STATE_ABR"
    if cond == "Destination State":
        return "DEST_STATE_ABR"
    if cond == "Distance":
        return "DISTANCE"
    if cond == "None":
        return "None"

#Compares data against given criteria and returns True or False
def meetsCriteria(Category, limiter, cond):
    if Category == "None":
        return True
    if Category == "Month":
        return limiter == getMonth(int(cond))
    if Category == "Origin City":
        return limiter == cond
    if Category == "Destination City":
        return limiter == cond
    if Category == "Carrier":
        return limiter == cond
    if Category == "Aircraft":
        return limiter == cond
    if Category == "Origin State":
        return limiter == cond
    if Category == "Destination State":
        return limiter == cond
    if Category == "Distance":
        return groupDistance(int(cond)) == distances.index(limiter)

#Assigns a distance value to one of the groups of distances
def groupDistance(distance):
    if distance in range(0,99):
        return 0
    if distance in range(100,199):
        return 1
    if distance in range(200,299):
        return 2
    if distance in range(300,399):
        return 3
    if distance in range(400,499):
        return 4
    if distance in range(500,999):
        return 5
    if distance in range(1000,1499):
        return 6
    if distance in range(1500,1999):
        return 7
    if distance in range(2000,2499):
        return 8
    if distance in range(2500,2999):
        return 9
    if distance in range(3000,3499):
        return 10
    if distance in range(3500,3999):
        return 11
    if distance in range(4000,4499):
        return 12
    if distance in range(4500,4999):
        return 13
    else:
         return -1

#Returns the name of a month given its number
def getMonth(number):
    if number == 1:
        return "January"
    if number == 2:
        return "February"
    if number == 3:
        return "March"
    if number == 4:
        return "April"
    if number == 5:
        return "May"
    if number == 6:
        return "June"
    if number == 7:
        return "July"
    if number == 8:
        return "August"
    if number == 9:
        return "September"
    if number == 10:
        return "October"
    if number == 11:
        return "November"
    if number == 12:
        return "December"

#Global Lists for the program
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
originCities = []
destCities = []
carriers = []
aircrafts = []
originStates = []
destStates = []
originStateDestStatePairs = []
carrierAircraftPairs = []
originCityAircraftPairs = []
distances = ["0-99","100-199","200-299","300-399","400-499","500-999","1000-1499","1500-1999","2000-2499","2500-2999","3000-3499","3500-3999","4000-4499","4500-4999"]
criteria = ["Top Ten", "Month", "Origin City", "Destination City", "Carrier", "Aircraft", "Distance", "Origin State", "Destination State"]


class Application(flightProgram.Frame):
    #defines the starting criteria
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    #Creates the select file button when the program starts
    def create_widgets(self):
        self.choose_file = flightProgram.Button(self)
        self.choose_file["text"] = "Choose Data File"
        self.choose_file["command"] = self.select_file
        self.choose_file.grid(row=0,column=0)

        self.quit = flightProgram.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row = 20, column =0)

    #Selects the file to be used by the program and creates the main menu
    def select_file(self):
        root.filename = flightProgram.filedialog.askopenfilename(initialdir = "/home/acc.cassidyj3/workspace/CSCI431", title = "Select file", filetypes = (("csv files", "*.csv"), ("all files", "*.*")))
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            #Populate the lists
            for row in reader:
                if row["ORIGIN_STATE_ABR"] not in originStates:
                    originStates.append(row["ORIGIN_STATE_ABR"])
                if row["ORIGIN_CITY_NAME"] not in originCities:
                    originCities.append(row["ORIGIN_CITY_NAME"])
                if row["DEST_STATE_ABR"] not in destStates:
                    destStates.append(row["DEST_STATE_ABR"])
                if row["DEST_CITY_NAME"] not in destCities:
                    destCities.append(row["DEST_CITY_NAME"])
                if row["UNIQUE_CARRIER_NAME"] not in carriers:
                    carriers.append(row["UNIQUE_CARRIER_NAME"])
                if row["AIRCRAFT_TYPE"] not in aircrafts:
                    aircrafts.append(row["AIRCRAFT_TYPE"])
                if [row['ORIGIN_STATE_ABR'],row['DEST_STATE_ABR']] not in originStateDestStatePairs:
                    originStateDestStatePairs.append([row['ORIGIN_STATE_ABR'],row['DEST_STATE_ABR']])
                if [row['UNIQUE_CARRIER_NAME'],['AIRCRAFT_TYPE']] not in carrierAircraftPairs:
                    carrierAircraftPairs.append([row['UNIQUE_CARRIER_NAME'],row['AIRCRAFT_TYPE']])
                if [row['ORIGIN_CITY_NAME'],['AIRCRAFT_TYPE']] not in originCityAircraftPairs:
                    originCityAircraftPairs.append([row['ORIGIN_CITY_NAME'],row['AIRCRAFT_TYPE']])
            #Sort the lists
            originCities.sort()
            originStates.sort()
            destCities.sort()
            destStates.sort()
            carriers.sort()
            aircrafts.sort()
        self.choose_file.destroy()
        self.defaults = flightProgram.Button(self)
        self.defaults["text"] = "Choose an automatic option"
        self.defaults["command"] = self.perform_defaults
        self.defaults.grid(row = 0, column =0)
        self.customs = flightProgram.Button(self)
        self.customs["text"] = "Enter your own options"
        self.customs["command"] = self.perform_customs
        self.customs.grid(row = 1, column =0)
        self.change_file = flightProgram.Button(self)
        self.change_file["text"] = "Change the data file"
        self.change_file["command"] = self.perform_change_file
        self.change_file.grid(row = 2, column =0)


    #Changes the data source file
    def perform_change_file(self):
        root.filename = flightProgram.filedialog.askopenfilename(initialdir = "/home/acc.cassidyj3/workspace/CSCI431", title = "Select file", filetypes = (("csv files", "*.csv"), ("all files", "*.*")))
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            #Clear lists
            originCities = []
            destCities = []
            carriers = []
            aircrafts = []
            originStates = []
            destStates = []
            originStateDestStatePairs = []
            carrierAircraftPairs = []
            originCityAircraftPairs = []
            #Repopulate Lists
            for row in reader:
                if row["ORIGIN_STATE_ABR"] not in originStates:
                    originStates.append(row["ORIGIN_STATE_ABR"])
                if row["ORIGIN_CITY_NAME"] not in originCities:
                    originCities.append(row["ORIGIN_CITY_NAME"])
                if row["DEST_STATE_ABR"] not in destStates:
                    destStates.append(row["DEST_STATE_ABR"])
                if row["DEST_CITY_NAME"] not in destCities:
                    destCities.append(row["DEST_CITY_NAME"])
                if row["UNIQUE_CARRIER_NAME"] not in carriers:
                    carriers.append(row["UNIQUE_CARRIER_NAME"])
                if row["AIRCRAFT_TYPE"] not in aircrafts:
                    aircrafts.append(row["AIRCRAFT_TYPE"])
                if [row['ORIGIN_STATE_ABR'],row['DEST_STATE_ABR']] not in originStateDestStatePairs:
                    originStateDestStatePairs.append([row['ORIGIN_STATE_ABR'],row['DEST_STATE_ABR']])
                if [row['UNIQUE_CARRIER_NAME'],['AIRCRAFT_TYPE']] not in carrierAircraftPairs:
                    carrierAircraftPairs.append([row['UNIQUE_CARRIER_NAME'],['AIRCRAFT_TYPE']])
                if [row['ORIGIN_CITY_NAME'],['AIRCRAFT_TYPE']] not in originCityAircraftPairs:
                    originCityAircraftPairs.append([row['ORIGIN_CITY_NAME'],['AIRCRAFT_TYPE']])
            #Sort Lists
            originCities.sort()
            originStates.sort()
            destCities.sort()
            destStates.sort()
            carriers.sort()
            aircrafts.sort()


    #Creates the menu for default options
    def perform_defaults(self):
        self.defaults.destroy()
        self.customs.destroy()
        self.change_file.destroy()
        self.result = flightProgram.Label(self, text = "")
        self.result.grid(row = 14, column =0)
        self.default_month = flightProgram.Button(self)
        self.default_month["text"] = "View best month to fly"
        self.default_month["command"] = self.perform_default_month
        self.default_month.grid(row = 0, column =0)
        self.default_aircraft = flightProgram.Button(self)
        self.default_aircraft["text"] = "View best aircraft to ride"
        self.default_aircraft["command"] = self.perform_default_aircraft
        self.default_aircraft.grid(row = 1, column =0)
        self.default_originState = flightProgram.Button(self)
        self.default_originState["text"] = "View best state to depart from"
        self.default_originState["command"] = self.perform_default_originState
        self.default_originState.grid(row = 2, column =0)
        self.default_originCity = flightProgram.Button(self)
        self.default_originCity["text"] = "View best city to depart from"
        self.default_originCity["command"] = self.perform_default_originCity
        self.default_originCity.grid(row = 3, column =0)
        self.default_distance = flightProgram.Button(self)
        self.default_distance["text"] = "View best distance to travel"
        self.default_distance["command"] = self.perform_default_distance
        self.default_distance.grid(row = 4, column =0)
        self.default_destState = flightProgram.Button(self)
        self.default_destState["text"] = "View best destination state"
        self.default_destState["command"] = self.perform_default_destState
        self.default_destState.grid(row = 5, column =0)
        self.default_destCity = flightProgram.Button(self)
        self.default_destCity["text"] = "View best destination city"
        self.default_destCity["command"] = self.perform_default_destCity
        self.default_destCity.grid(row = 6, column =0)
        self.default_carrier = flightProgram.Button(self)
        self.default_carrier["text"] = "View best carrier"
        self.default_carrier["command"] = self.perform_default_carrier
        self.default_carrier.grid(row = 7, column =0)
        self.default_topTen = flightProgram.Button(self)
        self.default_topTen["text"] = "View top ten flights"
        self.default_topTen["command"] = self.perform_defaultTop10
        self.default_topTen.grid(row = 8, column =0)
        self.default1 = flightProgram.Button(self)
        self.default1["text"] = "Best origin state/destination state pairing"
        self.default1["command"] = self.perform_default1
        self.default1.grid(row = 9, column =0)
        self.default2 = flightProgram.Button(self)
        self.default2["text"] = "Best aircraft/carrier pairing"
        self.default2["command"] = self.perform_default2
        self.default2.grid(row = 10, column =0)
        self.default3 = flightProgram.Button(self)
        self.default3["text"] = "Best origin city/aircraft pairing"
        self.default3["command"] = self.perform_default3
        self.default3.grid(row = 11, column =0)
        self.defaults_back = flightProgram.Button(self)
        self.defaults_back["text"] = "Return to menu"
        self.defaults_back["command"] = self.perform_defaults_back
        self.defaults_back.grid(row = 13, column =0)

    #Calculates the best month based on percentage of available scheduled seats
    def perform_default_month(self):
        MonthsData = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    MonthsData[int(row['MONTH']) - 1][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        MonthsData[int(row['MONTH']) - 1][1] += float(row['SEATS'])
        percentSeats = []
        for element in range(0,11):
            percentSeats.append(MonthsData[element][0] / MonthsData[element][1])
        if percentSeats.index(min(percentSeats)) == 0:
            self.result["text"] = "January is the best month to fly with " + str(100 - percentSeats[0] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 1:
            self.result["text"] = "February is the best month to fly with " + str(100 - percentSeats[1] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 2:
            self.result["text"] = "March is the best month to fly with " + str(100 - percentSeats[1] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 3:
            self.result["text"] = "April is the best month to fly with " + str(100 - percentSeats[3] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 4:
            self.result["text"] = "May is the best month to fly with " + str(100 - percentSeats[4] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 5:
            self.result["text"] = "June is the best month to fly with " + str(100 - percentSeats[5] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 6:
            self.result["text"] = "July is the best month to fly with " + str(100 - percentSeats[6] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 7:
            self.result["text"] = "August is the best month to fly with " + str(100 - percentSeats[7] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 8:
            self.result["text"] = "September is the best month to fly with " + str(100 - percentSeats[8] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 9:
            self.result["text"] = "October is the best month to fly with " + str(100 - percentSeats[9] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 10:
            self.result["text"] = "November is the best month to fly with " + str(100 - percentSeats[10] * 100) + " percent of seats available."
        if percentSeats.index(min(percentSeats)) == 11:
            self.result["text"] = "December is the best month to fly with " + str(100 - percentSeats[11] * 100) + " percent of seats available."

    #Calculates the best aircraft based on percentage of available scheduled seats
    def perform_default_aircraft(self):
        aircraftData = []
        for element in aircrafts:
            aircraftData.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    aircraftData[aircrafts.index(row['AIRCRAFT_TYPE'])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        aircraftData[aircrafts.index(row['AIRCRAFT_TYPE'])][1] += float(row['SEATS'])
        percentSeats = []
        for element in aircraftData:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = aircrafts[percentSeats.index(min(percentSeats))] + " is the best aircraft with " + str(100 - min(percentSeats) * 100) + " percent of seats available."

    #Calculate the best state to depart from based on percentage of available scheduled seats
    def perform_default_originState(self):
        originStateData = []
        for element in originStates:
            originStateData.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    originStateData[originStates.index(row['ORIGIN_STATE_ABR'])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        originStateData[originStates.index(row['ORIGIN_STATE_ABR'])][1] += float(row['SEATS'])
        percentSeats = []
        for element in originStateData:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = originStates[percentSeats.index(min(percentSeats))] + " is the best origin state with " + str(100 - min(percentSeats) * 100) + " percent of seats available."

    #Calculate the best city to depart from based on percentage of available scheduled seats
    def perform_default_originCity(self):
        originCityData = []
        for element in originCities:
            originCityData.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    originCityData[originCities.index(row['ORIGIN_CITY_NAME'])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        originCityData[originCities.index(row['ORIGIN_CITY_NAME'])][1] += float(row['SEATS'])
        percentSeats = []
        for element in originCityData:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = originCities[percentSeats.index(min(percentSeats))] + " is the best origin city with " + str(100 - (min(percentSeats) * 100)) + " percent of seats available."

    #Calculate the best travel distance
    def perform_default_distance(self):
        distanceData = []
        for element in distances:
            distanceData.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    distanceData[int(groupDistance(int(row['DISTANCE'])))][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        distanceData[int(groupDistance(int(row['DISTANCE'])))][1] += float(row['SEATS'])
        percentSeats = []
        for element in distanceData:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = str(distances[percentSeats.index(min(percentSeats))]) + " is the best travel distance with " + str(100 - (min(percentSeats) * 100)) + " percent of seats available."

    #Calculate the best destination state based on percentage of available scheduled seats
    def perform_default_destState(self):
        destStateData = []
        for element in destStates:
            destStateData.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    destStateData[destStates.index(row['DEST_STATE_ABR'])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        destStateData[destStates.index(row['DEST_STATE_ABR'])][1] += float(row['SEATS'])
        percentSeats = []
        for element in destStateData:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = destStates[percentSeats.index(min(percentSeats))] + " is the best destination state with " + str(100 - min(percentSeats) * 100) + " percent of seats available."

    #Calculate the best destination city based on percentage of available scheduled seats
    def perform_default_destCity(self):
        destCityData = []
        for element in destCities:
            destCityData.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    destCityData[destCities.index(row['DEST_CITY_NAME'])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        destCityData[destCities.index(row['DEST_CITY_NAME'])][1] += float(row['SEATS'])
        percentSeats = []
        for element in destCityData:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = destCities[percentSeats.index(min(percentSeats))] + " is the best destination city with " + str(100 - (min(percentSeats) * 100)) + " percent of seats available."

    #Calculate the best carrier based on percentage of available scheduled seats
    def perform_default_carrier(self):
        carrierData = []
        for element in carriers:
            carrierData.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    carrierData[carriers.index(row['UNIQUE_CARRIER_NAME'])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        carrierData[carriers.index(row['UNIQUE_CARRIER_NAME'])][1] += float(row['SEATS'])
        percentSeats = []
        for element in carrierData:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = carriers[percentSeats.index(min(percentSeats))] + " is the best carrier with " + str(100 - (min(percentSeats) * 100)) + " percent of seats available."

    #Gives information on the top ten flights overall
    #Clears all buttons and displays data, provides a new back button
    def perform_defaultTop10(self):
        topTen = []
        self.default1.destroy()
        self.default2.destroy()
        self.default3.destroy()
        self.defaults_back.destroy()
        self.default_month.destroy()
        self.default_aircraft.destroy()
        self.default_originState.destroy()
        self.default_originCity.destroy()
        self.default_distance.destroy()
        self.default_destState.destroy()
        self.default_destCity.destroy()
        self.default_carrier.destroy()
        self.default_topTen.destroy()
        self.result.destroy()
        self.top10Back = flightProgram.Button(self)
        self.top10Back["text"] = "Return to default option menu"
        self.top10Back["command"] = self.perform_top10Back
        self.top10Back.grid(row=0,column =0)
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    if len(topTen) == 0:
                        if float(row['DEPARTURES_PERFORMED']) != 0:
                            topTen.append([(float(row['PASSENGERS']) / float(row['SEATS'])), row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])
                        else:
                            topTen.append([1, row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])
                    else:
                        if float(row['DEPARTURES_PERFORMED'] != 0):
                            for attempt in range(0,len(topTen) - 1):
                                if (float(row['PASSENGERS']) / float(row['SEATS'])) < topTen[attempt][0]:
                                    topTen.insert(attempt, [(float(row['PASSENGERS']) / float(row['SEATS'])), row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])
                                    if len(topTen) > 10:
                                        del topTen[-1]
                                        break
                            if len(topTen) < 10:
                                if float(row['DEPARTURES_PERFORMED']) != 0:
                                    topTen.append([(float(row['PASSENGERS']) / float(row['SEATS'])), row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])
                                else:
                                    topTen.append([1, row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])

            self.top10OriginCityLabel = []
            self.top10OriginStateLabel = []
            self.top10DistanceLabel = []
            self.top10DestCityLabel = []
            self.top10DestStateLabel = []
            self.top10MonthLabel = []
            self.top10AircraftLabel = []
            self.top10CarrierLabel = []
            self.top10ScoreLabel = []
            self.top10OriginCityLabel.append(flightProgram.Label(self, text = "Origin City"))
            self.top10OriginStateLabel.append(flightProgram.Label(self, text = "Origin State"))
            self.top10DistanceLabel.append(flightProgram.Label(self, text = "Distance"))
            self.top10DestCityLabel.append(flightProgram.Label(self, text = "Destination City"))
            self.top10DestStateLabel.append(flightProgram.Label(self, text = "Destination State"))
            self.top10MonthLabel.append(flightProgram.Label(self, text = "Month"))
            self.top10AircraftLabel.append(flightProgram.Label(self, text = "Aircraft"))
            self.top10CarrierLabel.append(flightProgram.Label(self, text = "Carrier"))
            self.top10ScoreLabel.append(flightProgram.Label(self, text = "Percent Available Seats"))
            for element in topTen:
                self.top10OriginCityLabel.append(flightProgram.Label(self,text = element[1]))
                self.top10OriginStateLabel.append(flightProgram.Label(self,text = element[2]))
                self.top10DistanceLabel.append(flightProgram.Label(self,text = element[3]))
                self.top10DestCityLabel.append(flightProgram.Label(self,text = element[4]))
                self.top10DestStateLabel.append(flightProgram.Label(self,text = element[5]))
                self.top10MonthLabel.append(flightProgram.Label(self,text = getMonth(int(element[6]))))
                self.top10AircraftLabel.append(flightProgram.Label(self,text = element[7]))
                self.top10CarrierLabel.append(flightProgram.Label(self,text = element[8]))
                self.top10ScoreLabel.append(flightProgram.Label(self,text = str((1 - float(element[0]))*100)))
            for value in range(11):
                self.top10OriginCityLabel[value].grid(row = 1 + value, column = 0)
                self.top10OriginStateLabel[value].grid(row = 1 + value, column = 1)
                self.top10DistanceLabel[value].grid(row = 1 + value, column = 2)
                self.top10DestCityLabel[value].grid(row = 1 + value, column = 3)
                self.top10DestStateLabel[value].grid(row = 1 + value, column = 4)
                self.top10MonthLabel[value].grid(row = 1 + value, column = 5)
                self.top10AircraftLabel[value].grid(row = 1 + value, column = 6)
                self.top10CarrierLabel[value].grid(row = 1 + value, column = 7)
                self.top10ScoreLabel[value].grid(row = 1 + value, column = 8)

    #Returns to default menu from top ten display
    def perform_top10Back(self):
        for value in range(11):
            if len(self.top10OriginCityLabel) > value:
                self.top10OriginCityLabel[value].destroy()
                self.top10OriginStateLabel[value].destroy()
                self.top10DistanceLabel[value].destroy()
                self.top10DestCityLabel[value].destroy()
                self.top10DestStateLabel[value].destroy()
                self.top10MonthLabel[value].destroy()
                self.top10AircraftLabel[value].destroy()
                self.top10CarrierLabel[value].destroy()
                self.top10ScoreLabel[value].destroy()
        self.top10Back.destroy()
        self.result = flightProgram.Label(self, text = "")
        self.result.grid(row = 14, column =0)
        self.default_month = flightProgram.Button(self)
        self.default_month["text"] = "View best month to fly"
        self.default_month["command"] = self.perform_default_month
        self.default_month.grid(row = 0, column =0)
        self.default_aircraft = flightProgram.Button(self)
        self.default_aircraft["text"] = "View best aircraft to ride"
        self.default_aircraft["command"] = self.perform_default_aircraft
        self.default_aircraft.grid(row = 1, column =0)
        self.default_originState = flightProgram.Button(self)
        self.default_originState["text"] = "View best state to depart from"
        self.default_originState["command"] = self.perform_default_originState
        self.default_originState.grid(row = 2, column =0)
        self.default_originCity = flightProgram.Button(self)
        self.default_originCity["text"] = "View best city to depart from"
        self.default_originCity["command"] = self.perform_default_originCity
        self.default_originCity.grid(row = 3, column =0)
        self.default_distance = flightProgram.Button(self)
        self.default_distance["text"] = "View best distance to travel"
        self.default_distance["command"] = self.perform_default_distance
        self.default_distance.grid(row = 4, column =0)
        self.default_destState = flightProgram.Button(self)
        self.default_destState["text"] = "View best destination state"
        self.default_destState["command"] = self.perform_default_destState
        self.default_destState.grid(row = 5, column =0)
        self.default_destCity = flightProgram.Button(self)
        self.default_destCity["text"] = "View best destination city"
        self.default_destCity["command"] = self.perform_default_destCity
        self.default_destCity.grid(row = 6, column =0)
        self.default_carrier = flightProgram.Button(self)
        self.default_carrier["text"] = "View best carrier"
        self.default_carrier["command"] = self.perform_default_carrier
        self.default_carrier.grid(row = 7, column =0)
        self.default_topTen = flightProgram.Button(self)
        self.default_topTen["text"] = "View top ten flights"
        self.default_topTen["command"] = self.perform_defaultTop10
        self.default_topTen.grid(row = 8, column =0)
        self.default1 = flightProgram.Button(self)
        self.default1["text"] = "Best origin state/destination state pairing"
        self.default1["command"] = self.perform_default1
        self.default1.grid(row = 9, column =0)
        self.default2 = flightProgram.Button(self)
        self.default2["text"] = "Best carrier/aircraft pairing"
        self.default2["command"] = self.perform_default2
        self.default2.grid(row = 10, column =0)
        self.default3 = flightProgram.Button(self)
        self.default3["text"] = "Best origin city/aircraft pairing"
        self.default3["command"] = self.perform_default3
        self.default3.grid(row = 11, column =0)
        self.defaults_back = flightProgram.Button(self)
        self.defaults_back["text"] = "Return to menu"
        self.defaults_back["command"] = self.perform_defaults_back
        self.defaults_back.grid(row = 13, column =0)



    #Creates the menu for custom options
    def perform_customs(self):
        self.defaults.destroy()
        self.customs.destroy()
        self.change_file.destroy()
        self.result = flightProgram.Label(self, text = "")
        self.result.grid(row = 12, column =0)
        self.type1 = []
        self.type2 = []
        self.type3 = []
        for element in criteria:
            self.type1.append(element)
            self.type2.append(element)
            self.type3.append(element)
        self.type1.remove("Top Ten")
        self.type2.remove("Top Ten")
        self.type3.remove("Top Ten")
        self.type1.append("None")
        self.type2.append("None")
        self.type3.append("None")
        box1data = []
        box2data = []
        box3data = []
        self.chosenCriteria = flightProgram.StringVar()
        self.choice1 = flightProgram.StringVar()
        self.choice2 = flightProgram.StringVar()
        self.choice3 = flightProgram.StringVar()
        self.lim1 = flightProgram.StringVar()
        self.lim2 = flightProgram.StringVar()
        self.lim3 = flightProgram.StringVar()
        #First choice, determines whether you are viewing the top ten flights for a criteria, the best month, the best distance, etc.
        self.category = ttk.Combobox(self, textvariable = self.chosenCriteria, values = criteria)
        self.category.current(0)
        self.category.grid(row = 0, column = 0)
        #type of criteria to restrict by
        self.limitType1 = ttk.Combobox(self, textvariable = self.choice1, values = self.type1, postcommand = self.updtcblist1)
        self.limitType1.grid(row = 1, column = 0)
        self.limitType1.current(8)
        #value of criteria 2 to restrict by
        self.limiter1 = ttk.Combobox(self, textvariable = self.lim1, values = box1data, postcommand = self.updtcblista)
        self.limiter1.grid(row = 1, column = 1)
        #type of criteria to restrict by
        self.limitType2 = ttk.Combobox(self, textvariable = self.choice2, values = self.type2, postcommand = self.updtcblist2)
        self.limitType2.grid(row = 2, column = 0)
        self.limitType2.current(8)
        #value of criteria 2 to restrict by
        self.limiter2 = ttk.Combobox(self, textvariable = self.lim2, values = box2data, postcommand = self.updtcblistb)
        self.limiter2.grid(row = 2, column = 1)
        #type of criteria to restrict by
        self.limitType3 = ttk.Combobox(self, textvariable = self.choice3, values = self.type3, postcommand = self.updtcblist3)
        self.limitType3.grid(row = 3, column = 0)
        self.limitType3.current(8)
        #value of criteria 2 to restrict by
        self.limiter3 = ttk.Combobox(self, textvariable = self.lim3, values = box3data, postcommand = self.updtcblistc)
        self.limiter3.grid(row = 3, column = 1)
        self.confirm = flightProgram.Button(self)
        self.confirm["text"] = "Use currently selected options"
        self.confirm["command"] = self.perform_custom_check
        self.confirm.grid(row = 4, column = 0)
        self.customs_back = flightProgram.Button(self)
        self.customs_back["text"] = "Return to menu"
        self.customs_back["command"] = self.perform_customs_back
        self.customs_back.grid(row = 13, column =0)

    #Adjusts options in limiter1 based on contents of limitType1
    def updtcblista(self):
        box1data = []
        if self.choice1.get() == "Month":
            for element in months:
                box1data.append(element)
        if self.choice1.get() == "Origin City":
            for element in originCities:
                box1data.append(element)
        if self.choice1.get() == "Destination City":
            for element in destCities:
                box1data.append(element)
        if self.choice1.get() == "Carrier":
            for element in carriers:
                box1data.append(element)
        if self.choice1.get() == "Aircraft":
            for element in aircrafts:
                box1data.append(element)
        if self.choice1.get() == "Distance":
            for element in distances:
                box1data.append(element)
        if self.choice1.get() == "Origin State":
            for element in originStates:
                box1data.append(element)
        if self.choice1.get() == "Destination State":
            for element in destStates:
                box1data.append(element)
        self.limiter1['value'] = box1data

    #Adjusts options in limiter2 based on contents of limitType2
    def updtcblistb(self):
        box2data = []
        if self.choice2.get() == "Month":
            for element in months:
                box2data.append(element)
        if self.choice2.get() == "Origin City":
            for element in originCities:
                box2data.append(element)
        if self.choice2.get() == "Destination City":
            for element in destCities:
                box2data.append(element)
        if self.choice2.get() == "Carrier":
            for element in carriers:
                box2data.append(element)
        if self.choice2.get() == "Aircraft":
            for element in aircrafts:
                box2data.append(element)
        if self.choice2.get() == "Distance":
            for element in distances:
                box2data.append(element)
        if self.choice2.get() == "Origin State":
            for element in originStates:
                box2data.append(element)
        if self.choice2.get() == "Destination State":
            for element in destStates:
                box2data.append(element)
        self.limiter2['value'] = box2data

    #Adjusts options in limiter3 based on contents of limitType3
    def updtcblistc(self):
        box3data = []
        if self.choice3.get() == "Month":
            for element in months:
                box3data.append(element)
        if self.choice3.get() == "Origin City":
            for element in originCities:
                box3data.append(element)
        if self.choice3.get() == "Destination City":
            for element in destCities:
                box3data.append(element)
        if self.choice3.get() == "Carrier":
            for element in carriers:
                box3data.append(element)
        if self.choice3.get() == "Aircraft":
            for element in aircrafts:
                box3data.append(element)
        if self.choice3.get() == "Distance":
            for element in distances:
                box3data.append(element)
        if self.choice3.get() == "Origin State":
            for element in originStates:
                box3data.append(element)
        if self.choice3.get() == "Destination State":
            for element in destStates:
                box3data.append(element)
        self.limiter3['value'] = box3data

    #Updates options in limitType1 based on selections in limitType2, limitType3, and category
    def updtcblist1(self):
        self.type1 = []
        for element in criteria:
            self.type1.append(element)
        self.type1.remove("Top Ten")
        self.type1.append("None")
        if self.chosenCriteria.get() != "Top Ten":
            self.type1.remove(self.chosenCriteria.get())
        if self.choice3.get() != "None":
            self.type1.remove(self.choice3.get())
        if self.choice2.get() != "None":
            self.type1.remove(self.choice2.get())
        self.limitType1['value'] = self.type1

    #Updates options in limitType2 based on selections in limitType1, limitType3, and category
    def updtcblist2(self):
        self.type2 = []
        for element in criteria:
            self.type2.append(element)
        self.type2.remove("Top Ten")
        self.type2.append("None")
        if self.chosenCriteria.get() != "Top Ten":
            self.type2.remove(self.chosenCriteria.get())
        if self.choice1.get() != "None":
            self.type2.remove(self.choice1.get())
        if self.choice3.get() != "None":
            self.type2.remove(self.choice3.get())
        self.limitType2['value'] = self.type2

    #Updates options in limitType3 based on selections in limitType1, limitType2, and category
    def updtcblist3(self):
        self.type3 = []
        for element in criteria:
            self.type3.append(element)
        self.type3.remove("Top Ten")
        self.type3.append("None")
        if self.chosenCriteria.get() != "Top Ten":
            self.type3.remove(self.chosenCriteria.get())
        if self.choice1.get() != "None":
            self.type3.remove(self.choice1.get())
        if self.choice2.get() != "None":
            self.type3.remove(self.choice2.get())
        self.limitType3['value'] = self.type3

    #Uses the inputted criteria to make a check
    def perform_custom_check(self):
        if self.chosenCriteria.get() == "Top Ten":
            #Clears menu and displays top ten results under the given criteria
            topTen = []
            with open(root.filename) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                        if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                            for attempt in range(0,len(topTen) - 1):
                                if (float(row['PASSENGERS']) / float(row['SEATS'])) < topTen[attempt][0]:
                                    topTen.insert(attempt, [(float(row['PASSENGERS']) / float(row['SEATS'])), row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])
                                    if len(topTen) > 10:
                                        del topTen[-1]
                                        break
                            if len(topTen) < 10:
                                if float(row['DEPARTURES_PERFORMED']) != 0:
                                    topTen.append([(float(row['PASSENGERS']) / float(row['SEATS'])), row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])
                                else:
                                    topTen.append([1, row['ORIGIN_CITY_NAME'], row['ORIGIN_STATE_ABR'], row['DISTANCE'], row['DEST_CITY_NAME'], row['DEST_STATE_ABR'], row['MONTH'], row['AIRCRAFT_TYPE'], row['UNIQUE_CARRIER_NAME']])
            self.top10OriginCityLabel = []
            self.top10OriginStateLabel = []
            self.top10DistanceLabel = []
            self.top10DestCityLabel = []
            self.top10DestStateLabel = []
            self.top10MonthLabel = []
            self.top10AircraftLabel = []
            self.top10CarrierLabel = []
            self.top10ScoreLabel = []
            self.top10OriginCityLabel.append(flightProgram.Label(self, text = "Origin City"))
            self.top10OriginStateLabel.append(flightProgram.Label(self, text = "Origin State"))
            self.top10DistanceLabel.append(flightProgram.Label(self, text = "Distance"))
            self.top10DestCityLabel.append(flightProgram.Label(self, text = "Destination City"))
            self.top10DestStateLabel.append(flightProgram.Label(self, text = "Destination State"))
            self.top10MonthLabel.append(flightProgram.Label(self, text = "Month"))
            self.top10AircraftLabel.append(flightProgram.Label(self, text = "Aircraft"))
            self.top10CarrierLabel.append(flightProgram.Label(self, text = "Carrier"))
            self.top10ScoreLabel.append(flightProgram.Label(self, text = "Percent Available Seats"))
            self.result.destroy()
            self.confirm.destroy()
            self.customs_back.destroy()
            self.category.destroy()
            self.limitType1.destroy()
            self.limitType2.destroy()
            self.limitType3.destroy()
            self.limiter1.destroy()
            self.limiter2.destroy()
            self.limiter3.destroy()
            for element in topTen:
                self.top10OriginCityLabel.append(flightProgram.Label(self,text = element[1]))
                self.top10OriginStateLabel.append(flightProgram.Label(self,text = element[2]))
                self.top10DistanceLabel.append(flightProgram.Label(self,text = element[3]))
                self.top10DestCityLabel.append(flightProgram.Label(self,text = element[4]))
                self.top10DestStateLabel.append(flightProgram.Label(self,text = element[5]))
                self.top10MonthLabel.append(flightProgram.Label(self,text = getMonth(int(element[6]))))
                self.top10AircraftLabel.append(flightProgram.Label(self,text = element[7]))
                self.top10CarrierLabel.append(flightProgram.Label(self,text = element[8]))
                self.top10ScoreLabel.append(flightProgram.Label(self,text = str((1 - float(element[0]))*100)))
            for value in range(11):
                if len(topTen) > value:
                    self.top10OriginCityLabel[value].grid(row = 1 + value, column = 0)
                    self.top10OriginStateLabel[value].grid(row = 1 + value, column = 1)
                    self.top10DistanceLabel[value].grid(row = 1 + value, column = 2)
                    self.top10DestCityLabel[value].grid(row = 1 + value, column = 3)
                    self.top10DestStateLabel[value].grid(row = 1 + value, column = 4)
                    self.top10MonthLabel[value].grid(row = 1 + value, column = 5)
                    self.top10AircraftLabel[value].grid(row = 1 + value, column = 6)
                    self.top10CarrierLabel[value].grid(row = 1 + value, column = 7)
                    self.top10ScoreLabel[value].grid(row = 1 + value, column = 8)
            self.custom10Back = flightProgram.Button(self)
            self.custom10Back['text'] = "Return to option selection"
            self.custom10Back['command'] = self.perform_custom10Back
            self.custom10Back.grid(row = 0, column = 0)

        else:
            #calculates and displays the best option in the selected category for the limiting criteria
            comparison = []
            grouping = []
            columnName = ""
            cond1 = ""
            cond2 = ""
            cond3 = ""
            if self.chosenCriteria.get() == "Distance":
                #Performs the calculation for distance
                for element in distances:
                    comparison.append([0,0])
                with open(root.filename) as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                            if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                comparison[groupDistance(int(row['DISTANCE']))][0] += float(row['PASSENGERS'])
                                if float(row['DEPARTURES_PERFORMED']) != 0:
                                    comparison[groupDistance(int(row['DISTANCE']))][1] += float(row['SEATS'])


            else:
                #calculations for everything else
                if self.chosenCriteria.get() == "Month":
                    i = 1
                    for element in months:
                        comparison.append([0,0])
                        grouping.append(str(i))
                        i+=1
                    with open(root.filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                                if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                    comparison[grouping.index(row['MONTH'])][0] += float(row['PASSENGERS'])
                                    if float(row['DEPARTURES_PERFORMED']) != 0:
                                        comparison[grouping.index(row['MONTH'])][1] += float(row['SEATS'])
                if self.chosenCriteria.get() == "Origin City":
                    for element in originCities:
                        comparison.append([0,0])
                        grouping.append(element)
                    with open(root.filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                                if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                    comparison[grouping.index(row['ORIGIN_CITY_NAME'])][0] += float(row['PASSENGERS'])
                                    if float(row['DEPARTURES_PERFORMED']) != 0:
                                        comparison[grouping.index(row['ORIGIN_CITY_NAME'])][1] += float(row['SEATS'])
                if self.chosenCriteria.get() == "Destination City":
                    for element in destCities:
                        comparison.append([0,0])
                        grouping.append(element)
                    with open(root.filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                                if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                    comparison[grouping.index(row['DEST_CITY_NAME'])][0] += float(row['PASSENGERS'])
                                    if float(row['DEPARTURES_PERFORMED']) != 0:
                                        comparison[grouping.index(row['DEST_CITY_NAME'])][1] += float(row['SEATS'])
                if self.chosenCriteria.get() == "Carrier":
                    for element in carriers:
                        comparison.append([0,0])
                        grouping.append(element)
                    with open(root.filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                                if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                    comparison[grouping.index(row['UNIQUE_CARRIER_NAME'])][0] += float(row['PASSENGERS'])
                                    if float(row['DEPARTURES_PERFORMED']) != 0:
                                        comparison[grouping.index(row['UNIQUE_CARRIER_NAME'])][1] += float(row['SEATS'])
                if self.chosenCriteria.get() == "Aircraft":
                    for element in aircrafts:
                        comparison.append([0,0])
                        grouping.append(element)
                    with open(root.filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                                if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                    comparison[grouping.index(row['AIRCRAFT_TYPE'])][0] += float(row['PASSENGERS'])
                                    if float(row['DEPARTURES_PERFORMED']) != 0:
                                        comparison[grouping.index(row['AIRCRAFT_TYPE'])][1] += float(row['SEATS'])
                if self.chosenCriteria.get() == "Origin State":
                    for element in originStates:
                        comparison.append([0,0])
                        grouping.append(element)
                        columnName = "ORIGIN_STATE_ABR"
                    with open(root.filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                                if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                    comparison[grouping.index(row['ORIGIN_STATE_ABR'])][0] += float(row['PASSENGERS'])
                                    if float(row['DEPARTURES_PERFORMED']) != 0:
                                        comparison[grouping.index(row['ORIGIN_STATE_ABR'])][1] += float(row['SEATS'])
                if self.chosenCriteria.get() == "Destination State":
                    for element in destStates:
                        comparison.append([0,0])
                        grouping.append(element)
                    with open(root.filename) as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            if validateRow(int(row['DEPARTURES_SCHEDULED']),int(row['SEATS'])):
                                if meetsCriteria(self.choice1.get(), self.lim1.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice2.get(), self.lim2.get(), row[translate(self.choice1.get())]) and meetsCriteria(self.choice3.get(), self.lim3.get(), row[translate(self.choice1.get())]):
                                    comparison[grouping.index(row['DEST_STATE_ABR'])][0] += float(row['PASSENGERS'])
                                    if float(row['DEPARTURES_PERFORMED']) != 0:
                                        comparison[grouping.index(row['DEST_STATE_ABR'])][1] += float(row['SEATS'])
                percentScores = []
                for value in comparison:
                    if value[1] != 0:
                        percentScores.append(value[0]/value[1])
                    else:
                        percentScores.append(1)
            if self.chosenCriteria.get() == "Month":
                #Month gets filtered out due to a small difference in content to get meaningful results (month name instead of number)
                self.result["text"] = "The best " + self.chosenCriteria.get() + " for the given criteria is " + months[(percentScores.index(min(percentScores)))+1] + " with " + str(100 - (100 * min(percentScores))) + " percent of seats available."
            else:
                self.result["text"] = "The best " + self.chosenCriteria.get() + " for the given criteria is " + grouping[percentScores.index(min(percentScores))] + " with " + str(100 - (100 * min(percentScores))) + " percent of seats available."

    #Returns from custom options top ten display to custom options menu
    def perform_custom10Back(self):
        for value in range(11):
            if len(self.top10OriginCityLabel) > value:
                self.top10OriginCityLabel[value].destroy()
                self.top10OriginStateLabel[value].destroy()
                self.top10DistanceLabel[value].destroy()
                self.top10DestCityLabel[value].destroy()
                self.top10DestStateLabel[value].destroy()
                self.top10MonthLabel[value].destroy()
                self.top10AircraftLabel[value].destroy()
                self.top10CarrierLabel[value].destroy()
                self.top10ScoreLabel[value].destroy()
        self.custom10Back.destroy()
        self.result = flightProgram.Label(self, text = "")
        self.result.grid(row = 12, column =0)
        self.type1 = []
        self.type2 = []
        self.type3 = []
        for element in criteria:
            self.type1.append(element)
            self.type2.append(element)
            self.type3.append(element)
        self.type1.remove("Top Ten")
        self.type2.remove("Top Ten")
        self.type3.remove("Top Ten")
        self.type1.append("None")
        self.type2.append("None")
        self.type3.append("None")
        box1data = []
        box2data = []
        box3data = []
        self.chosenCriteria = flightProgram.StringVar()
        self.choice1 = flightProgram.StringVar()
        self.choice2 = flightProgram.StringVar()
        self.choice3 = flightProgram.StringVar()
        self.lim1 = flightProgram.StringVar()
        self.lim2 = flightProgram.StringVar()
        self.lim3 = flightProgram.StringVar()
        self.category = ttk.Combobox(self, textvariable = self.chosenCriteria, values = criteria)
        self.category.current(0)
        self.category.grid(row = 0, column = 0)
        self.limitType1 = ttk.Combobox(self, textvariable = self.choice1, values = self.type1, postcommand = self.updtcblist1)
        self.limitType1.grid(row = 1, column = 0)
        self.limitType1.current(8)
        self.limiter1 = ttk.Combobox(self, textvariable = self.lim1, values = box1data, postcommand = self.updtcblista)
        self.limiter1.grid(row = 1, column = 1)
        self.limitType2 = ttk.Combobox(self, textvariable = self.choice2, values = self.type2, postcommand = self.updtcblist2)
        self.limitType2.grid(row = 2, column = 0)
        self.limitType2.current(8)
        self.limiter2 = ttk.Combobox(self, textvariable = self.lim2, values = box2data, postcommand = self.updtcblistb)
        self.limiter2.grid(row = 2, column = 1)
        self.limitType3 = ttk.Combobox(self, textvariable = self.choice3, values = self.type3, postcommand = self.updtcblist3)
        self.limitType3.grid(row = 3, column = 0)
        self.limitType3.current(8)
        self.limiter3 = ttk.Combobox(self, textvariable = self.lim3, values = box3data, postcommand = self.updtcblistc)
        self.limiter3.grid(row = 3, column = 1)
        self.confirm = flightProgram.Button(self)
        self.confirm["text"] = "Use currently selected options"
        self.confirm["command"] = self.perform_custom_check
        self.confirm.grid(row = 4, column = 0)
        self.customs_back = flightProgram.Button(self)
        self.customs_back["text"] = "Return to menu"
        self.customs_back["command"] = self.perform_customs_back
        self.customs_back.grid(row = 13, column =0)

    #Returns to the main menu from the custom option menu
    def perform_customs_back(self):
        self.customs_back.destroy()
        self.category.destroy()
        self.limitType1.destroy()
        self.limiter1.destroy()
        self.limitType2.destroy()
        self.limiter2.destroy()
        self.limitType3.destroy()
        self.limiter3.destroy()
        self.result.destroy()
        self.defaults = flightProgram.Button(self)
        self.defaults["text"] = "Choose an automatic option"
        self.defaults["command"] = self.perform_defaults
        self.defaults.grid(row = 0, column =0)
        self.customs = flightProgram.Button(self)
        self.customs["text"] = "Enter your own options"
        self.customs["command"] = self.perform_customs
        self.customs.grid(row = 1, column =0)
        self.change_file = flightProgram.Button(self)
        self.change_file["text"] = "change the data file"
        self.change_file["command"] = self.perform_change_file
        self.change_file.grid(row = 15, column =0)

    #Returns to the main menu from the default option menu
    def perform_defaults_back(self):
        self.default1.destroy()
        self.default2.destroy()
        self.default3.destroy()
        self.defaults_back.destroy()
        self.default_month.destroy()
        self.default_aircraft.destroy()
        self.default_originState.destroy()
        self.default_originCity.destroy()
        self.default_distance.destroy()
        self.default_destState.destroy()
        self.default_destCity.destroy()
        self.default_carrier.destroy()
        self.default_topTen.destroy()
        self.result.destroy()
        self.defaults = flightProgram.Button(self)
        self.defaults["text"] = "Choose an automatic option"
        self.defaults["command"] = self.perform_defaults
        self.defaults.grid(row = 0, column =0)
        self.customs = flightProgram.Button(self)
        self.customs["text"] = "Enter your own options"
        self.customs["command"] = self.perform_customs
        self.customs.grid(row = 1, column =0)
        self.change_file = flightProgram.Button(self)
        self.change_file["text"] = "change the data file"
        self.change_file["command"] = self.perform_change_file
        self.change_file.grid(row = 15, column =0)

    #Calculates the best pair of origin state and destination state
    def perform_default1(self):
        data = []
        for element in originStateDestStatePairs:
            data.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    data[originStateDestStatePairs.index([row['ORIGIN_STATE_ABR'],row['DEST_STATE_ABR']])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        data[originStateDestStatePairs.index([row['ORIGIN_STATE_ABR'],row['DEST_STATE_ABR']])][1] += float(row['SEATS'])
        percentSeats = []
        for element in data:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = originStateDestStatePairs[percentSeats.index(min(percentSeats))][0] + ", " + originStateDestStatePairs[percentSeats.index(min(percentSeats))][1] + " is the best origin state/destination state pair with " + str(100 - (min(percentSeats) * 100)) + " percent of seats available."


    #Calculates the best pair of carrier and aircraft
    def perform_default2(self):
        data = []
        for element in carrierAircraftPairs:
            data.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    data[carrierAircraftPairs.index([row['UNIQUE_CARRIER_NAME'],row['AIRCRAFT_TYPE']])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        data[carrierAircraftPairs.index([row['UNIQUE_CARRIER_NAME'],row['AIRCRAFT_TYPE']])][1] += float(row['SEATS'])
        percentSeats = []
        for element in data:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = carrierAircraftPairs[percentSeats.index(min(percentSeats))][0] + ", " + carrierAircraftPairs[percentSeats.index(min(percentSeats))][1] + " is the best carrier/aircraft pair with " + str(100 - (min(percentSeats) * 100)) + " percent of seats available."

    #Calculates the best pair of origin city and aircraft
    def perform_default3(self):
        data = []
        for element in originCityAircraftPairs:
            data.append([0,0])
        with open(root.filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if validateRow(float(row['DEPARTURES_SCHEDULED']), float(row['SEATS'])):
                    data[originCityAircraftPairs.index([row['ORIGIN_CITY_NAME'],row['AIRCRAFT_TYPE']])][0] += float(row['PASSENGERS'])
                    if float(row['DEPARTURES_PERFORMED']) != 0:
                        data[originCityAircraftPairs.index([row['ORIGIN_CITY_NAME'],row['AIRCRAFT_TYPE']])][1] += float(row['SEATS'])
        percentSeats = []
        for element in data:
            if element[1] != 0:
                percentSeats.append(element[0] / element[1])
            else:
                percentSeats.append(1)
        self.result["text"] = originCityAircraftPairs[percentSeats.index(min(percentSeats))][0] + ", " + originCityAircraftPairs[percentSeats.index(min(percentSeats))][1] + " is the best origin city/aircraft pair with " + str(100 - (min(percentSeats) * 100)) + " percent of seats available."


root = flightProgram.Tk()
app = Application(master=root)
app.mainloop()


def main():
    return 0

# call the main function to start the program
if __name__== "__main__":
    main()
