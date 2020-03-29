
"""
Created on Thu Aug 29 22:08:48 2019

"""
import math

dictOfSubjects = {
  'DM' : 0,
  'NLP': 1,
  'AI': 2, 
  'SDA' : 3,
 'IP' : 4,
  'BD' : 5,
  'GM' : 6,
  'ML' : 7,
  'EC' : 8,
  'WMC' : 9,
  'CC' : 10
}

Studentcount = 11
class AssignSubjects: 
  
    # Initialize variables 
    def __init__(self): 
  
            self.allmask = 0
  
            self.total_subjects = 11
  
            self.allocationsub = [[0 for i in range(Studentcount)] for j in range(self.total_subjects)] 
            
                 
    def countWaysUtil(self,dp): 
          
        mask = self.allmask-1

            
        for mask in range(self.allmask-1,-1,-1):
            #find the student
            ppl=mask           
            student_no=0
            # If all students are assigned a topic so we 
            # are done and this is one way so return 1 
            if mask==self.allmask:
                return 1              
            
            # If not everyone is assigned a topic and also there are no more 
            # topics left to process, so there is no way, thus return 0; 
            if self.total_subjects > 11:
                return 0
            
            # If we have already solved this subproblem, return the answer.
            #  if (dp[mask]!= -1 ): 
            #   return dp[mask]
        
            # assign ith topic one by one  to all the possible students 
            # and recur for remaining subjects. 
            while(ppl):
                student_no+=(ppl & 1)
                ppl=ppl/2
                ppl=math.floor(ppl)
            for subject_no in range(0,Studentcount):
                # if student 'student' has not already taken the subject 
                # but has selected the subject as one of the options move forward
                if (not( mask & (1<<subject_no)) and self.allocationsub[student_no][subject_no]):
                    #Save the resuklt of the student taking the subject and move forward
                    dp[mask]+=dp[mask | (1<<subject_no)]
            
        #display the result            
        # print("The total number of allocations possible is: ",dp[mask])
        Allocations= dp[mask]
        
        #Write the allocations to outputPS4.txt
        f=open("outputPS4.txt","w+",1)
        f.write("The total number of allocations possible is: " + str(Allocations))
        
    def countWays(self): 
  
        # Reads n lines from standard input for current test case 
        # create dictionary for Subjects. Subject[i] = list of person having     
        array2D = []
        with open('inputPS4.txt', 'r') as f:
            for line in f.readlines():
                if line.rstrip():
                    line=line.strip('\n')
                    array2D.append(line.split(' / '))
                
          #  print (array2D)
        for ppl in range(Studentcount): 
            for i in range(1, len(array2D[ppl])):
                sub_selected = dictOfSubjects[array2D[ppl][i]]
                self.allocationsub[ppl][sub_selected]=1

        # allmask is used to check if all persons 
        # are included or not, set all n bits as 1 
        #print (self.allocationsub)
        self.allmask= (1 << Studentcount)
        
        # Initialize all entries in dp as 0 and the final entry as 1
        dp = [0] * self.allmask;
        dp[self.allmask-1]=1
        self.countWaysUtil(dp)
        
       
def main(): 
   #No_of_people = input() # number of persons in every test case 
   # number of persons in every test case 
   AssignSubjects().countWays()    
if __name__ == '__main__':
             main()
  