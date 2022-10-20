import numbers
from re import X
from tkinter import END, TOP, font
from tracemalloc import start
from turtle import left, position, width
from xml.etree.ElementInclude import include
from manim import *


class LinearFunction(Scene):
    def construct(self):

        rastucaLF = MathTex("{f: y = ax + b}", font_size=50).to_edge(UL) # vytvorím si matematický text, pre vzorec lineárnej funkcie, veľkosť nastavím na 50, pozíciu na UL(Up Left)
        rastucaLF.set_color(YELLOW) 
        rastucaLF[0][4].set_color(RED) # musia byť 2 [v prvej je neviem čo] , [v druhej je pozícia meneného písmena] - nastavím farbu na RED
        rastucaLF[0][7].set_color(RED) 

        konkretnyVzorecLF = MathTex('{f: y = y * 1}', font_size=50).to_edge(UL).set_color(YELLOW)
        konkretnyVzorecLF[0][4].set_color(RED)
        konkretnyVzorecLF[0][6].set_color(RED)


        rastucaHoreVzorecLF = MathTex('{f: y = y + 1}', font_size=50).to_edge(UL).set_color(YELLOW)
        konstantnaVzorecLF = MathTex('{f: y = 1}', font_size=50).to_edge(UL).set_color(YELLOW)




        arrow1 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(rastucaLF[0][4], DOWN)
        arrow2 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(rastucaLF[0][7], DOWN)
        arrows= Group(arrow1, arrow2)
        arrow3 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(rastucaLF, DOWN)

        konkretnyVzorecText = Text("Rastúca lineárna funkcia", font_size=25).next_to(arrow3, DOWN)


        cislaab = MathTex("{a, b \in R}").next_to(arrow2, DOWN).shift(LEFT*0.5)             # to /in je v dokumentacií pre symboly pre LaTex
        

        text1 = Text("""Vytvoríme si novú súradnicovú os.""",  
        t2c={"súradnicovú os": BLUE},           # t2 asi znamená nejaké zobrazenie to (t2)- c   c-čko znamená asi color - mením farbu na BLUE ???
        t2s={"súradnicovú os": ITALIC}          # t2 asi znamená nejaké zobrazenie to (t2) - s   s-ko znamená asi style - mením štýl na ITALIC ???
        ).scale(0.7).next_to(rastucaLF)         # scale je veľkosť a zobrazujem ju vedľa textu rastucaLF
        
        text2 = Text("""Na zostrojenie nám stačia 2 body """, font_size=30).to_corner(DR)
        text2[22].set_color(RED)

        boxLinFunkcie = SurroundingRectangle(rastucaLF, color=WHITE, buff=0.3)               # vytváram obldĺžnik, ktorý bude obkresľovať vzorec
                                    
        
        suradnicovaOs = Axes(                                                                 # vytvorim súradnicovú os s nejakými parametrami
            x_range=[-8,8,1],
            y_range=[-8,8,1],
            tips=False,
            x_length=10,
            y_length=10,
           
            axis_config=
            {
            "stroke_color": GREY_A,
            "include_numbers": True,
            }
        )


       # INY ZAPIS PRE ZISKANIE SURADNICE BODU bod2 = Dot(np.array([0, 0, 0]), color=YELLOW)

        # TOTO BY MAL BYT (1,2) - to jest SURADNICE BODOV KTORE SA ZAPISU KU BODU annos[f"{1}{2}"] = TexMobject(f"({1}, {2})")
        bod1 = Dot(suradnicovaOs.coords_to_point(2,2), color=YELLOW)
        bodkociarka1 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(2,2))
        
     
        bod2 = Dot(np.array([0, 0, 0]), color=YELLOW)

        bod3 = Dot(suradnicovaOs.coords_to_point(0,1), color=YELLOW)
        bodkociarka4 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(0,1))

        bod4 = Dot(suradnicovaOs.coords_to_point(-2,-1), color=YELLOW)
        bodkociarka4 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(-2,-1))

       #  bod5= Dot(suradnicovaOs.coords_to_point(0,1), color=YELLOW)
       #  bodkociarka5 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(0,1))

       #  bod6= Dot(suradnicovaOs.coords_to_point(1,0), color=YELLOW)
       #  bodkociarka6 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(1,0))

        #  y: -2*y -3
        rastucaHoreGrafLF = suradnicovaOs.plot(lambda y: y + 1 * 1, x_range=[-5,4])
        konkretnyGrafLF = suradnicovaOs.plot(lambda y: y*1, x_range=[-4,4])

        konstantnaGrafLF = suradnicovaOs.plot(lambda y: 1 , x_range=[-8,8])

        y_label = suradnicovaOs.get_y_axis_label("y").shift(UP*0.1, LEFT)
        x_label = suradnicovaOs.get_x_axis_label("x").next_to(suradnicovaOs)
        grid_labels = VGroup(x_label, y_label)

       # self.play(*[FadeOut(mobj) for mobj in self.mobjects])  vsetky veci co som urobil z obrazovky zmiznu

    
        self.play(Write(text1))                                                                 # zobrazenie textu vytvoríme súradnicovú os
        self.play(Write(suradnicovaOs), run_time=3)                                                        # vytvorí nám súradnicovú os
        self.play(FadeOut(text1))                                                               # nechám text zmiznúť
        
        self.play(Create(rastucaLF))  
        self.play(Create(boxLinFunkcie))                                                            
        self.wait()
       
        
        self.play(FadeIn(arrows))
        self.play(Create(cislaab))

    
        self.play(FadeIn(bod1, bod2, bodkociarka1, grid_labels))
       
        self.play(FadeOut(boxLinFunkcie,arrows, cislaab))
        self.play(ClockwiseTransform(rastucaLF, konkretnyVzorecLF))
        self.play(Create(konkretnyGrafLF))
        self.play(Write(arrow3))
        self.play(Write(konkretnyVzorecText))
        
       
        self.play(Write(text2))
        self.play(FadeOut(bod1, bod2, bodkociarka1)) 
        self.play(FadeIn(bod3, bod4, bodkociarka4))
        self.play(FadeOut(text2))
        
        self.play(FadeTransformPieces(konkretnyGrafLF, rastucaHoreGrafLF))

        #POSUN FUNKCIE O +1 na Y-ovej osi
        self.play(FadeOut(rastucaLF,arrow3))
        self.play(ClockwiseTransform(konkretnyVzorecText, rastucaHoreVzorecLF))
        self.wait()
        
        #self.play(FadeIn(bod5,bod6,bodkociarka5,bodkociarka6))
        self.play(FadeOut(bod3, bod4, bodkociarka4,))

        self.play(ClockwiseTransform(konkretnyVzorecText, konstantnaVzorecLF))
   
        self.play(ReplacementTransform(rastucaHoreGrafLF, konstantnaGrafLF))

     

        # Konstantna funkcia

       
        
       

     
        
                                                                          


        
        
        
        
        
