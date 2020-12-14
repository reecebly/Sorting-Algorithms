# pygame applicaiton
import pygame
import random
pygame.init()

# setitng dimensions and name of window
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Sorting Algorithms")

#array that we will use for sorting
unsortedArray = [200, 140, 60, 80, 110, 90, 170, 50, 30, 185, 300, 440,
                 30, 250, 410, 390, 70, 50, 300, 285, 360, 140, 10, 200,
                 290, 90, 170, 20, 30, 185, 444, 333, 222, 111, 30, 75]

#starting coordinates for bottom left of the itms in the array
x = 40
y = 550

#set type of font and size
font = pygame.font.Font('freesansbold.ttf', 20)
# main colors
background = (61,77,102)
foreground = (144,181,240)
white = (255,255,255)

title = font.render('Sorting Algorithms', True, foreground, background)
titleRect = title.get_rect()
titleRect.center = (100, 20)

quick = font.render('Quicksort: 1', True, white, background)
quickRect = quick.get_rect()
quickRect.center = (275, 20)

bubble = font.render('Bubblesort: 2', True, foreground, background)
bubbleRect = bubble.get_rect()
bubbleRect.center = (420, 20)

select = font.render('Selectsort: 3', True, white, background)
selectRect = select.get_rect()
selectRect.center = (570, 20)

scramble = font.render('Scramble Array: Space', True, foreground, background)
scrambleRect = scramble.get_rect()
scrambleRect.center = (765, 20)

width = window.get_width()

# stores the height of the
# screen into a variable
height = window.get_height()

#width of bars
width = 20

#takes two items in an array and swaps their positions
def swap(positionOne: int, positionTwo: int, arr):
    temp = arr[positionOne]
    arr[positionOne] = arr[positionTwo]
    arr[positionTwo] = temp

#selection sort algorithm
def selectionSort(arr):
    for i in range(len(arr)):
        # Looking for smallest element in array
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        #swap i and min, then update display
        swap(i, min, arr)
        displayUpdate(arr)

#sorts array using bubble sort algorithm
def bubbleSort(unsortedArray):
    isFullySorted = True
    sortedArray = unsortedArray
    length = len(sortedArray)

    for i in range(length - 1):
        if sortedArray[i] > sortedArray[i + 1]:
            swap(i, i + 1, sortedArray)
            isFullySorted = False
    displayUpdate(unsortedArray)

    if isFullySorted:
        return(sortedArray)
    else:
        return(bubbleSort(sortedArray))

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low , high):

        #is current smaller than pivot
        if arr[j] < pivot:

            #increment index of smaller element
            i = i + 1
            swap(i, j, arr)

    swap(i + 1, high, arr)
    return (i + 1)

#quick sort algorithm
def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        displayUpdate(unsortedArray)

        #sort before and after partition separately
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

#displays all the items in the array
def displayArray(height):
    for i in range(len(height)):
        pygame.draw.rect(window, (144, 181, 240), (x + 30 * i, y - height[i], width, height[i]))

def displayUpdate(arr):
    window.fill((61, 77, 102))
    window.blit(title, titleRect)
    window.blit(quick, quickRect)
    window.blit(bubble, bubbleRect)
    window.blit(select, selectRect)
    window.blit(scramble, scrambleRect)
    displayArray(arr)
    pygame.time.delay(200)
    pygame.display.update()

def scrambleArray(arr):
    random.shuffle(arr)
    displayUpdate(arr)

#driver function
def main():

    #flag for running GUI applicaiton
    isRunning = True

    while isRunning:

        executeSort = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            executeSort = True
            quickSort(unsortedArray, 0, 35)
            executeSort = False

        if keys[pygame.K_2]:
            executeSort = True
            bubbleSort(unsortedArray)

        if keys[pygame.K_3]:
            executeSort = True
            selectionSort(unsortedArray)

        if keys[pygame.K_SPACE]:
            executeSort == True
            scrambleArray(unsortedArray)

        if executeSort == False:
            displayUpdate(unsortedArray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #close project
                isRunning = False
    else:
        pygame.quit()

main()
