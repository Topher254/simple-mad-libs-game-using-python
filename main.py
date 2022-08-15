# this is a madlib program
# First I will start with the story.
# the story is about my life as a small child when I started studying. I will describe what I loved the most and what I always did after school
# the words in braces are my answers
my_story = '''
when I was a small child, My favorite meal was {favorite}
I used to {walk1} to my neighbor houses.
I was a {cry} baby. 
I love {myself} so much.
'''
favorite_meal = input("What can you eat while hungry?: ")
walk = input("An action to let you move from one place to another : ")
cry = input("What you do to relieve yourself: ")
myself1 = input("Something that you love: ")
# next i have to put the data that I have collected in a tuple
story_tuple = ()
MyStoryList = list(story_tuple) # I am converting th tuple to a string so that Ican be able to append the data that I receive from the input
MyStoryList.append(favorite_meal)
MyStoryList.append(walk)
MyStoryList.append(cry)
MyStoryList.append(myself1)
story_tuple = tuple(MyStoryList) # I then convert the list back to a tuple since I have to use a tuple
print(my_story.format(favorite=story_tuple[0], walk1=story_tuple[1], cry=story_tuple[2], myself=story_tuple[3]))
# For the output I am using a .format string concatenation method whereby I am Accessing the input data i  the tuples then I am able to output them in my story
# Run it and enjoy the Mad lib game script
