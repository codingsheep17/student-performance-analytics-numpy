import numpy as np
import matplotlib.pyplot as plt

class StudentsAnalytics:
    def main(self):
        try:
            self.data = np.loadtxt('students.csv', 
                    delimiter=',', 
                    skiprows=1, 
                    usecols=(5,6,7), 
                    dtype=str)
            self.data_clean = np.char.strip(self.data, '"')
            self.arr = self.data_clean.astype(float)
            self.user_menu()
        except Exception as f:
            print(f"Error, While Initializaiton {f}")
        
    
    def user_menu(self):
        running = True
        while running:
            try:
                self.user_menu_choice = int(input("""\n===== Student Performance Analytics Tool =====
1. Show basic statistics (mean, min, max, std) per subject
2. Show top 5 students
3. Show per-student total & average score
4. Show gender-wise and group-wise averages
5. Show score distribution (histogram)
6. Exit
==============================================
Enter your choice:"""))
            except Exception as e:
                print("Kindly Enter Only Number (1-6)")
            if self.user_menu_choice == 1:
                self.basic_stats()
            elif self.user_menu_choice == 2:
                self.top_students()
            elif self.user_menu_choice == 3:
                self.avg_students()
            elif self.user_menu_choice == 4:
                print("Thanks For Using!! Bye.")
                running = False
        
    def basic_stats(self):
        means   = np.mean(self.arr, axis=0)   # one mean per subject
        medians = np.median(self.arr, axis=0)   # one median per subject
        mins    = np.min(self.arr, axis=0)  # one min per subject
        maxs    = np.max(self.arr, axis=0)  # one max per subject
        stds    = np.std(self.arr, axis=0)  # one std per subject
        self.subjects = ["Math", "Reading", "Writing"]
        print("\n===== Basic Statistics =====")
        print("Subject\tMean\tMedian\tMin\tMax\tStd")
        for i, subj in enumerate(self.subjects):
            print(f"{subj}\t{means[i]:.2f}\t{medians[i]:.2f}\t{mins[i]:.2f}\t{maxs[i]:.2f}\t{stds[i]:.2f}")

    def top_students(self):
        try:
            self.topstd_choice = int(input("""===== Top Students =====
1: Per Subject Toppers (top 5)
2: Overall Toppers (top 5)
Enter Your Choice: """))
            if self.topstd_choice == 1:
                self.math = np.argsort(self.arr[:, 0])[-5:][::-1]
                self.reading =  np.argsort(self.arr[:, 1])[-5:][::-1]
                self.writing = np.argsort(self.arr[:, 2])[-5:][::-1]
                for i in self.math:
                    print(f"""Maths: ID {i}: {self.arr[i, 0]}""")
                print("**************************************")
                for j in self.reading:
                    print(f"""Reading: ID {j}: {self.arr[j, 1]}""")
                print("**************************************")
                for k in self.writing:
                    print(f"""Wrting: ID {k}: {self.arr[k, 2]}""")
                print("**************************************")
                
            elif self.topstd_choice == 2:
                self.toppers = np.sum(self.arr, axis=1)
                self.totals = np.argsort(self.toppers)[-5:][::-1]
                for j in self.totals:
                    print(f"""ID {j}: Total-{self.toppers[j]}, Math-{self.arr[j, 0]}, Reading-{self.arr[j, 1]}, Writing-{self.arr[j, 2]}""")
        except Exception as t:
            print(f"Kindly Enter Only Numbers (1-2), {t}")
            
    def avg_students(self):
        for idx,j in enumerate(range(0, self.arr.shape[0])):
            pass_or_fail = np.where(np.sum(self.arr[idx]) > 99, "Pass", "Fail")
            print(f"ID:{j}, Total= {np.sum(self.arr[idx])}, Average= {np.average(self.arr[idx]):.2f}, Status = {pass_or_fail} ")
        
        totals = self.arr.sum(axis=1)
        averages = np.round(self.arr.mean(axis=1), 2)
        status = np.where(totals > 99, "Pass", "Fail")
        output = np.column_stack([self.arr, totals, averages, status])
        try:
            self.file_save_choice = str(input("Do You Want To Save in new File? (y/n): ")).lower()
            if self.file_save_choice == 'y':
                print("Content Saved Into A new .csv File!!")
                np.savetxt("student_analysis.csv", output, delimiter=",", fmt="%s",
                header="Math,Reading,Writing,Total,Average,Status", comments="")
            else:
                print("Error Couldn't Save to the file!")
        except Exception as e:
            print(f"Error {e}")    
    
if __name__=="__main__":
    students_analytics = StudentsAnalytics()
    students_analytics.main()