
from manimlib.imports import *



class BubbleSortScene(Scene):
    SORT_WAIT_TIME=0.2
    def construct(self):
        title = TexMobject("\left( Bubble \\right) \quad Sort")
        description = TextMobject(
            "Swaps adjacent elements of a list \\\\ until the maximum element reaches the end of the list"
            ,organize_left_to_right=True
        )
        VGroup(title,description).arrange(DOWN)        
        self.play(Write(title))
        self.play(Write(description))
        self.wait(2.5)
        
        self.play(FadeOut(title))
        self.play(description.to_edge,UP)
        self.wait()
        # self.play(FadeOut(description))
  
        self.input_array = [2,9,1,4,7,8,6,5,3]
        self.indexes = [i for i in range(len(self.input_array))]
        self.tex_array = self.wrap_input_array()
        self.v_array = VGroup(*self.tex_array).arrange(buff=LARGE_BUFF)
        
        self.circles = [Circle() for i in self.input_array]
        
        for index,c in enumerate(self.circles):
            c.surround(self.v_array[index])
            self.v_array[index].add(c)

        # self.add(*self.circles)
        self.play(ShowCreation(self.v_array))
        self.wait()
        self.bubble_sort()
        self.play(FadeOut(self.v_array))
        self.play(FadeOut(description))
        end_note=TextMobject("Thanks for watching the video \\\\ The code for generating the animation is in the description")
        self.play(ShowCreation(end_note))
        self.wait()
        self.play(FadeOut(end_note))
        self.wait()
        



    def wrap_input_array(self):
        return [TexMobject(str(i))
            for i in self.input_array
        ]
    
    def bubble_sort(self):
        for i in range(len(self.input_array)):
            for j in range(len(self.input_array) - i - 1):
                if (self.input_array[j] > self.input_array[j+1]):
                    self.act(j,j+1)
    def act(self,i,j):
        # print(self.input_array)
        # print(self.indexes)
        # print(i,j)
        self.play(Swap(self.v_array[self.indexes[i]],self.v_array[self.indexes[j]] ))
        self.wait(BubbleSortScene.SORT_WAIT_TIME)
        BubbleSortScene.SORT_WAIT_TIME*=0.7
        self.input_array[i],self.input_array[j] = self.input_array[j],self.input_array[i]
        self.indexes[i],self.indexes[j] = self.indexes[j],self.indexes[i]
