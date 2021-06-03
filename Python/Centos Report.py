#!/usr/bin/env python3

'''
OPS435 Assignment 2 - Summer 2020
Program: a2_cfribeiro-batinga.py
Author: Caio Batinga
The python code in this file a2_cfribeiro-batinga.py is original work written by
Caio Batinga. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.

'''

import os
import sys
import time
import argparse
import subprocess

args = object()  # arguments will be returned here from parse_command_args()

def parse_command_args():  
    "Calls argumentparser, and returns an object"
    
    parser = argparse.ArgumentParser(description="Usage Report based on the last command",epilog="Copyright 2020 - Caio Batinga")
    parser.add_argument("-l", "--list", type=str, choices=['user','host'], help="generate user name or remote host IP from the given files")
    parser.add_argument("-r", "--rhost", help="usage report for the given remote host IP")
    parser.add_argument("-t", "--type", choices=['daily','monthly'], help="type of report: daily or monthly") #Added daily and montly reports
    parser.add_argument("-u", "--user", help="usage report for the given user name")
    parser.add_argument("-s", "--seconds", action="store_true", help="return times in seconds")
    parser.add_argument("-v","--verbose", action="store_true",help="turn on output verbosity")
    parser.add_argument("files",metavar='F', type=str, nargs='+',help="list of files to be processed")
    args=parser.parse_args()

    if args.verbose:
        print('Files to be processed:',args.files)
        print('Type of args for files',type(args.files))
        if args.user:
            print('usage report for user:',args.user)
        if args.rhost:
            print('usage report for remote host:',args.rhost)
        if args.type:
            print('usage report type:',args.type)
    return args

def open_file_list():  
    "opens each file from args, and returns a list of lines"
    output = []
    filename_list = args.files
    if 'F' in filename_list:
        filename_list.remove('F')
    #TODO: if args.files contains 'online', use Popen to call `last -Fiw
    if 'online' in args.files:
        run = os.popen("last -Fiw")   # Run command in background
        user_list = run.readlines() # Read the output
        run.close()
        users = []
        for user in user_list:
            if len(user.split()) == 15:
                users.append(user)
        return users
        
    for filename in args.files:  # several files could be specified
        f = open(filename, 'r')
        output = f.read().split('\n')
        f.close()
    return output  # this is a LIST

def parse_for_user(file_line_list):  
    "call this function when 'a2_<st_id>.py -l user'"
    return_set = set()
    for line in file_line_list:
        if line == '':
            pass
        else:
            splitted = line.split()
            return_set.add(splitted[0])
    return_list = list(return_set)
    return_list.sort()
    return return_list

def parse_for_host(file_line_list):  # definition specified
    "call this function when 'a2_<st_id>.py -l host'"

    return_list = []
    return_set = set()
    for line in file_line_list:
        if line == '':  # if the line is empty, ignore it
            pass
        else:
            splitted = line.split()
            return_set.add(splitted[2])
    return_list = list(return_set)  # convert this to a list, and
    return_list.sort()  # sort alphabetically
    return return_list

def parse_for_daily(output_list, user):  
    "call this when user uses -u/r <user/ip> -t daily"
    return_dict = {}
    total = 0
    # for each line in output list:
    for userline in output_list:
        if userline == '':# if the line is empty, ignore it
            pass
        else:
            if user in userline:
                dates = extract_date(userline) # use extract_date to get the start date and stop date.
            
                if dates == '': #if dates is empty ignores
                    pass
                else:
                    
                    time = return_duration_secs(dates[0],dates[1])


                    day = return_date_str(dates[0])
                    if day in return_dict:
                        return_dict[day] += time #Increment to the key 
                    else:
                        return_dict[day] = time # New Key
                    total += time

    return return_dict

def extract_date(line):  
    "get dates from a line of output"
    if line == '':
        return None
    else:
        outlist = []
        splitted = line.split()
        first_date = splitted[4:8]
        second_date = splitted[10:14]
        t_in = " ".join(first_date)
        t_out = " ".join(second_date)
        try:
            fmt="%b %d %H:%M:%S %Y"
            time_in = time.strptime(t_in, fmt)
            time_out = time.strptime(t_out, fmt)
            outlist.append(time_in)
            outlist.append(time_out)
        except:
            return None
        return outlist

def return_date_str(date_object):  
    "take in date object, return as string in DD/MM/YYYY"
    fmt="%d/%m/%Y"
    return str(time.strftime(fmt, date_object))

def return_duration_secs(start_time, stop_time): 
    "take two date objects, return the difference between them in seconds"
    fl_stop = int(time.strftime("%s", stop_time))
    fl_start = int(time.strftime("%s", start_time))
    return fl_stop - fl_start

def convert_hours(seconds):
    hours = str(time.strftime('%H:%M:%S', time.gmtime(seconds))) #Return HH:MM:SS
    return hours
    

def print_report(usereport):

        print("Date                Usage")
        total = 0
        if not args.seconds:
            for day in usereport:
                total += usereport[day]
                print(day, '   ', convert_hours(usereport[day]))# Convert to HH:MM:SS
            print("Total        ", convert_hours(total))

        else:
            for day in usereport:
                total += usereport[day]
                print(day, '   ', usereport[day])
            print("Total        ", str(total))

if __name__ == "__main__":
    args = parse_command_args()
    output = open_file_list()

    if args.list == 'user':
        userlist = parse_for_user(output) #gets user list and sends to parse
        print("\nUser list for " + str(args.files[0]))
        print("=============================\n")
        print("\n".join(userlist))
    if args.list == 'host':
        userlist = parse_for_host(output)
        print("\nHost list for " + str(args.files[0]))
        print("=============================")
        print("\n".join(userlist))
    if args.user:
        usereport = parse_for_daily(output,args.user)
        print("\nDaily usage report for " + str(args.user))
        print("=============================")
        print_report(usereport)

    if args.rhost:
        usereport = parse_for_daily(output,args.rhost)
        print("\nDaily usage report for " + str(args.rhost))
        print("=============================")
        print_report(usereport)



        
    
        

    # check args.user
    # call proper function
    # create a function to display the output
    # output for user list should have one column
    # output for daily/monthly reports should have 2 columns
