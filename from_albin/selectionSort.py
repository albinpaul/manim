
from manimlib.imports import *

class SelectionSortScene(Scene):
    SORT_WAIT_TIME=0.2
    def construct(self):
        title = TexMobject("\left( Selection Sort \\right)")
        description = TextMobject("Selection sort select minimum element from a sub-array \\\\ and the swaps with the current element in a loop \\\\ Let's see this in action")
        self.add_sound("Luxery_trimmed")
        VGroup(title,description).arrange(DOWN)        
        self.play(Write(title))
        self.play(Write(description))
        self.play(FadeOut(title))
        self.wait()
        self.play(FadeOut(description))
        self.wait(4)

        self.input_array = [2,9,1,4,7,8,6,5,3]
        self.tex_array = self.wrap_input_array()
        self.circles = [Circle(color = BLUE) for i in self.input_array]
        for index,c in enumerate(self.circles):
            c.surround(self.tex_array[index])
            self.tex_array[index].add(c)

        self.v_array = VGroup(*self.tex_array).arrange(buff=MED_LARGE_BUFF)
        self.play(ShowCreation(self.v_array))
        self.wait()
        self.brace = None
        self.tip = None
        self.selection_sort()
        self.wait()
        self.play(FadeOut(self.v_array))
        end_note=TextMobject("Thanks for watching the video \\\\ The code for generating the animation is in the description")
        end_frame_box = SurroundingRectangle(end_note, buff = .6, color = RED)
        self.play(ShowCreation(end_note))
        self.play(ShowCreation(end_frame_box))
        self.wait(2.5)
        self.play(FadeOut(end_frame_box))
        self.play(FadeOut(end_note))
        

    def wrap_input_array(self):
        return [TexMobject(str(i), fill_color=WHITE)
            for i in self.input_array
        ]
    
    def selection_sort(self):
        for i in range(len(self.input_array)):
            minimum_index = i
            for j in range(i+1,len(self.input_array)):
                if (self.input_array[minimum_index] > self.input_array[j]):
                    minimum_index = j
            if (i != minimum_index):        
                self.act(i,minimum_index)
        self.play(FadeOut(self.t1),
            FadeOut(self.brace),
            FadeOut(self.tip)
        )
    
    def swap(self,i,j):
        self.v_array.generate_target()
        self.v_array.target[i].move_to(self.v_array[j])
        self.v_array.target[j].move_to(self.v_array[i])
        self.play(MoveToTarget(self.v_array,  path_arc=90 * DEGREES))
        self.v_array.submobjects[i],self.v_array.submobjects[j] = \
            self.v_array.submobjects[j],self.v_array.submobjects[i]
        self.v_array.arrange(buff=MED_LARGE_BUFF)
        # self.add_sound("Wood_Plank_Flicks")
        self.add_sound("Instrument_Strum")
        
    def act(self,i,j):
        text = "Smallest number \\\\ in this range is chosen \\ and swapped out"
        if not self.brace:
            self.brace = Brace(self.v_array[i+1:],UP,buff=SMALL_BUFF)
            self.t1 = self.brace.get_text(text)
            self.tip = ArrowTip(
                start_angle= 90 * DEGREES,
                color=RED,
            )
            self.tip.next_to(self.v_array[j],direction=DOWN)
            self.play(FadeInFrom(self.tip, DOWN))
            self.play(GrowFromCenter(self.brace))
            self.play(FadeIn(self.t1))     
        else:
            b2 = Brace(self.v_array[i+1:],UP,buff=SMALL_BUFF)
            
            self.tip.next_to(self.v_array[j],direction=DOWN)
            next_tip = ArrowTip(
                start_angle= 90 * DEGREES,
                color=RED,
            )
            next_tip.next_to(self.v_array[j],direction = DOWN)
            self.play(
                Transform(self.brace, b2),
                Transform(self.t1, b2.get_text(text)),
                Transform(self.tip, next_tip)
            )
            
        self.swap(i,j)
        self.input_array[i],self.input_array[j] = self.input_array[j],self.input_array[i] 

                