import sys
import operator

#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  f = open('suc_ph.csv' , 'r')
  suc_reg = {}
  for index, line in enumerate (f):
    row = line.split(',')
    if row[0] not in suc_reg:
      suc_reg[row[0]] = 1
    else:
      suc_reg[row[0]] = suc_reg[row[0]] + 1

    
  suc_list = sorted(suc_reg.items(), key=operator.itemgetter(1), reverse=True)
  print "1. The region with the most SUC is ",suc_list[0][0]

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  if school_year == '2010-2011':
    syear = 2
  elif school_year == '2011-2012':
    syear = 3
  elif school_year == '2012-2013':
    syear = 4
    
  f = open('suc_ph.csv' , 'r')
  suc_reg = {}
  for index, line in enumerate (f):
      row = line.split(',')
      #print row[2]
      if row[0] != 'region' and row[syear].strip() != '-':
        if row[0] in suc_reg:
          suc_reg[row[0]] += int(row[syear])
        else:
          suc_reg[row[0]] = int(row[syear])
  #print suc
  f.close()
  suc_list = sorted(suc_reg.items(), key = operator.itemgetter(1), reverse = True)
  print '2. The region with the most SUC enrollees is ' + suc_list[0][0]

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  if school_year == '2009-2010':
    syear = 5
  elif school_year == '2010-2011':
    syear = 6
  elif school_year == '2011-2012':
    syear = 7

  f = open('suc_ph.csv' , 'r')
  suc_reg = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[0] != 'region' and row[syear].strip() != '-':
        if row[0] in suc_reg:
          suc_reg[row[0]] += int(row[syear])
        else:
          suc_reg[row[0]] = int(row[syear])
  f.close()
  suc_list = sorted(suc_reg.items(), key = operator.itemgetter(1), reverse = True)
  #print suc_list
  print "3. The region with the most SUC graduates is " + suc_list[0][0]

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  suc_reg = {}
  if school_year == '2010-2011' and level == 'BS':
    syear = 2
  elif school_year == '2011-2012' and level == 'BS':
    syear = 5
  elif school_year == '2012-2013' and level == 'BS':
    syear = 8

  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  suc_reg = {}
  for index, line in enumerate (f):
      row = line.split(',')
      if row[syear] != 'first_sem_2010-2011_bs_ab' and row[syear].isdigit() == True:
        suc_reg[row[1]] = int(row[syear])
  f.close()
  suc_list = sorted(suc_reg.items(), key = operator.itemgetter(1))
  #for x in range(len(suc_list)):
  #  print suc_list[x][0],suc_list[x][1]
  print "4. Top 3 cheapest SUC for ",level," level in school year ",school_year
  print "  1. ",suc_list[0][0]
  print "  2. ",suc_list[1][0]
  print "  3. ",suc_list[2][0]

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  suc_reg = {}
  if school_year == '2010-2011' and level == 'BS':
    syear = 2
  elif school_year == '2011-2012' and level == 'BS':
    syear = 5
  elif school_year == '2012-2013' and level == 'BS':
    syear = 8

  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  for index, line in enumerate (f):
      row = line.split(',')
      if row[syear] != 'first_sem_2010-2011_bs_ab' and row[syear].isdigit() == True:
        suc_reg[row[1]] = int(row[syear])
  f.close()
  suc_list = sorted(suc_reg.items(), key = operator.itemgetter(1),reverse=True)

  #for x in range(20):
  #  print suc_list[x][0],suc_list[x][1]
  print "5. Top 3 expensive SUC for ",level," level in school year ",school_year
  print "  1. ",suc_list[0][0]
  print "  2. ",suc_list[1][0]
  print "  3. ",suc_list[2][0]
  #print "5. Top 3 expensive SUC for BS level in school year 2010-2011"
  #print "  1. Technological University of the Philippines"
  #print "  2. Marikina Polytechnic College"
  #print "  3. Apayao State College"

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  suc = []
  #suc_static = []
  syear10_11 = 2
  syear11_12 = 5
  syear12_13 = 8 
  f = open('tuitionfeeperunitsucproglevel20102013.csv' , 'r')
  for index, line in enumerate (f):
      row = line.split(',')
      if row[syear10_11] != 'first_sem_2010-2011_bs_ab' and  row[syear10_11].isdigit() == True and row[syear11_12].isdigit() == True and row[syear12_13].isdigit() == True:
        if row[syear10_11] < row[syear11_12] or row[syear10_11] < row[syear12_13]:
          suc.append(row[1])
        #else:
          #suc_static.append(row[1])
  f.close()
  #x = ", ".join(suc_static)
  s = ", ".join(suc)
  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  print "\" "+ s + " \""
  
  #print "   Technological University of the Philippines, Apayao State College, Marikina Polytechnic College, Surigao State College of Technology"

#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  suc_reg = {}
  if school_year == '2010-2011':
    syear = 3
  elif school_year == '2011-2012':
    syear = 4
  elif school_year == '2012-2013':
    syear = 5

  f = open('performancesucprclicensureexam20102012.csv' , 'r')
  for index, line in enumerate (f):
      row = line.split(',')
      if row[0] != 'region' and row[syear].strip() != '-':
        suc_reg[row[2]] = int(row[syear])
  f.close()
  suc_list = sorted(suc_reg.items(), key = operator.itemgetter(1),reverse=True)

  print "7. The discipline which has the highest passing rate is ",suc_list[0][0]

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  suc_reg = {}
  if school_year == '2010' and discipline == 'Accountancy':
    syear = 3
  elif school_year == '2011' and discipline == 'Accountancy':
    syear = 4
  elif school_year == '2012' and discipline == 'Accountancy':
    syear = 5

  f = open('performancesucprclicensureexam20102012.csv' , 'r')
  for index, line in enumerate (f):
      row = line.split(',')
      if row[0] != 'region' and row[syear].strip() != '-' and row[2] == 'Accountancy':
        suc_reg[row[1]] = int(row[syear])
  f.close()
  suc_list = sorted(suc_reg.items(), key = operator.itemgetter(1),reverse=True)
  #for x in range(20):
    #print suc_list[x][0],suc_list[x][1]
  print "8. Top 3  SUC with highest passing rate in ",discipline," for school year 2010-",school_year
  print "  1. ",suc_list[0][0]
  print "  2. ",suc_list[1][0]
  print "  3. ",suc_list[2][0]
  #print "8. Top 3  SUC with highest passing rate in Accountancy for school year 2010-2011"
  #print "  1. Technological University of the Philippines"
  #print "  2. Marikina Polytechnic College"
  #print "  3. Apayao State College"



def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010-2011')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()