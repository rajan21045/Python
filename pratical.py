# generate random marks for 20 students in 5 subjects 
# find each student's total marks and average marks
# indetify top 3 students
# calculate subject-wise highest, lowest and average marks
# normalize marks to scale ( like converting to percentage or z score )

import numpy as np
import random
# Step 1: Generate random marks for 20 students in 5 subjects
num_students = 20
num_subjects = 5
marks = np.random.randint(0, 101, size=(num_students, num_subjects))

# finding total marks and average marks for each student
total_marks_per_student = np.sum(marks, axis=1)
average_marks_per_student = np.mean(marks, axis=1)
print("Total Marks per Student:", total_marks_per_student)
print("Average Marks per Student:", average_marks_per_student)


# Step 2: Identify top 3 students based on total marks
top_3_students = np.argsort(total_marks_per_student)[-3:][::-1]
print("\nTop 3 Students (by total marks)")
for rank, idx in enumerate(top_3_students, start=1):
    print(f"Rank {rank}: Student {idx + 1} with Total Marks = {total_marks_per_student[idx]}")


#  step 4
# Calculate subject-wise highest, lowest and average marks
highest_marks_per_subject = np.max(marks, axis=0)
lowest_marks_per_subject = np.min(marks, axis=0)
average_sub = np.mean(marks, axis=0)
print("\nSubject-wise Highest Marks:", highest_marks_per_subject)
print("Subject-wise Lowest Marks:", lowest_marks_per_subject)
print("Subject-wise Average Marks:", np.round(average_sub,2))

# Step 5: Normalize marks to scale (percentage)
percentage = (marks / 100) * 100
print("\nPercentage Marks (Normalized 0 to 100):\n", np.round(percentage,2))

# Z-score Normalization
z_scores = (marks - np.mean(marks)) / np.std(marks)
print("\nZ-score Normalized Marks:\n", np.round(z_scores,2))


class_average = np.mean(total_marks_per_student)
above_average_students = np.where(total_marks_per_student > class_average)[0]
print("\nStudent Above Average Students (Total Marks > Class Average):", above_average_students)
