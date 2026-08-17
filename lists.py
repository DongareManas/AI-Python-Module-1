subjects = ["Python", "AI", "ML", "Data Science"]
print(subjects)
print(subjects[0])
# ADD 
subjects.append("Deep Learning")
print(subjects)

# Remove
subjects.remove("AI")
print(subjects)

#Loop through list
print("\n")
for subject in subjects:
    print(subject)