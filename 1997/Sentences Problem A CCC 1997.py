num_of_sets=int(input('Enter number of sets: '))

for current_set in range(num_of_sets):

    num_of_subjects=int(input('Enter number of subjects: '))
    num_of_verbs=int(input('Enter number of verbs: '))
    num_of_objects=int(input('Enter number of objects: '))

    subjects=[input('Enter subject: ') for subject in range(num_of_subjects)]
    verbs=[input('Enter verb: ') for subject in range(num_of_verbs)]
    objects=[input('Enter object: ') for subject in range(num_of_objects)]

    for subject in range(num_of_subjects):
        for verb in range(num_of_verbs):
            for object1 in range(num_of_objects):
                sentence=subjects[subject]+' '+verbs[verb]+' '+objects[object1]+'.'
                print(sentence)
        
