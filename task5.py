# displaying the no. of days in a month
p=str(input(" enter the month "))
s=p.lower()
if ( s=='april' or s=='june' or s=='september' or s=='november' ):
    print(" the no. of days ", str(30))
elif (s=='february'):
    print(" the no. of days= ", str(28))
elif (s=='january' or s=='march' or s=='may' or s=='july' or s=='august' or s=='october' or s=='december'):
    print(" the no. of days= ", str(31))
else:
    print(" Invalid ")
