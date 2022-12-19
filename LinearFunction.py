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

        konkretnyVzorecLF = MathTex('{f: y = 1x+0}', font_size=50).to_edge(UL).set_color(YELLOW)
        konkretnyVzorecLF[0][4].set_color(RED)
        konkretnyVzorecLF[0][7].set_color(RED)


        arrow1 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(rastucaLF[0][4], DOWN)
        arrow2 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(rastucaLF[0][7], DOWN)
        arrows= Group(arrow1, arrow2)
        arrow3 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(rastucaLF, DOWN)

        konstantnaLFVzorecText = Tex('Ak ' , '$a = 0 $' ,' je to konštantná lineárna funkcia', font_size=25).next_to(arrow3, DOWN).shift(RIGHT*0.65)
        konstantnaLFVzorecText[1].set_color(RED).scale(1)
        rastucaLFVzorecText = Tex('Ak ' , '$a > 0 $' ,' je to rastúca lineárna funkcia', font_size=25).next_to(arrow3, DOWN).shift(RIGHT*0.65)
        rastucaLFVzorecText[1].set_color(RED).scale(1)
        klesajucaVzorecText = Tex('Ak ' , '$a < 0 $' ,' je to klesajúca lineárna funkcia', font_size=25).next_to(arrow3, DOWN).shift(RIGHT*0.65)
        klesajucaVzorecText[1].set_color(RED).scale(1)


        cislaab = MathTex("{a, b \in R}").next_to(arrow2, DOWN).shift(LEFT*0.5)              # to /in je v dokumentacií pre symboly pre LaTex
        cislaab[0][0].set_color(RED)
        cislaab[0][2].set_color(RED)         
        

        text1 = Text("Lineárna Funkcia",  
        t2c={"Lineárna": YELLOW, "Funkcia":RED}           
        )       
        
        text2 = Text("""Na zostrojenie nám stačia 2 body """, font_size=30).to_corner(DR)
        text2[22].set_color(RED)

        boxLinFunkcie = SurroundingRectangle(rastucaLF, color=WHITE, buff=0.3)              
                                    
        
        suradnicovaOs = Axes(                                                                 
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
        
        konkretnyGrafLFnula = suradnicovaOs.plot(lambda y: 0*y+0, x_range=[-8,8])
       

        konkretnyVzorecLFnula = MathTex('{f: y = 0x+0}', font_size=50).to_edge(UL).set_color(YELLOW)
        bodNula1 = Dot(suradnicovaOs.coords_to_point(2,0), color=YELLOW)
        bodNula2 = Dot(suradnicovaOs.coords_to_point(-2,0), color=YELLOW)
        konkretnyVzorecLFnula[0][4].set_color(RED)
        konkretnyVzorecLFnula[0][7].set_color(RED)

        konkretnyGrafLFplus1 = suradnicovaOs.plot(lambda y: 1*y+0, x_range=[-6,6])
        konkretnyVzorecLFplus1 = MathTex('{f: y = 1x+0}', font_size=50).to_edge(UL).set_color(YELLOW)
        bod1Plus1= Dot(suradnicovaOs.coords_to_point(1,1), color=YELLOW)
        bodkociarka1Plus1 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(1,1))
        bod2Plus1= Dot(suradnicovaOs.coords_to_point(-1,-1), color=YELLOW)
        bodkociarka2Plus1 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(-1,-1))
        konkretnyVzorecLFplus1[0][4].set_color(RED)
        konkretnyVzorecLFplus1[0][7].set_color(RED)

        konkretnyGrafLFplus2 = suradnicovaOs.plot(lambda y: 2*y+0, x_range=[-4,4])
        konkretnyVzorecLFplus2 = MathTex('{f: y = 2x+0}', font_size=50).to_edge(UL).set_color(YELLOW)
        bod1Plus2= Dot(suradnicovaOs.coords_to_point(1,2), color=YELLOW)
        bodkociarka1Plus2 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(1,2))
        bod2Plus2= Dot(suradnicovaOs.coords_to_point(-1,-2), color=YELLOW)
        bodkociarka2Plus2 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(-1,-2))
        konkretnyVzorecLFplus2[0][4].set_color(RED)
        konkretnyVzorecLFplus2[0][7].set_color(RED)

        konkretnyGrafLFplus3 = suradnicovaOs.plot(lambda y: 3*y+0, x_range=[-4,4])
        konkretnyVzorecLFplus3 = MathTex('{f: y = 3x+0}', font_size=50).to_edge(UL).set_color(YELLOW)

        bod1Plus3= Dot(suradnicovaOs.coords_to_point(1,3), color=YELLOW)
        bodkociarka1Plus3 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(1,3))
        bod2Plus3= Dot(suradnicovaOs.coords_to_point(-1,-3), color=YELLOW)
        bodkociarka2Plus3 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(-1,-3))

        konkretnyVzorecLFplus3[0][4].set_color(RED)
        konkretnyVzorecLFplus3[0][7].set_color(RED)

        konkretnyGrafLFminus1 = suradnicovaOs.plot(lambda y: -1*y+0, x_range=[-4,6])
        konkretnyVzorecLFminus1 = MathTex('{f: y = -1x+0}', font_size=50).to_edge(UL).set_color(YELLOW)
        bod1Minus1= Dot(suradnicovaOs.coords_to_point(-1,1), color=YELLOW)
        bodkociarka1Minus1 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(-1,1))
        bod2Minus1= Dot(suradnicovaOs.coords_to_point(1,-1), color=YELLOW)
        bodkociarka2Minus1 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(1,-1))
        konkretnyVzorecLFminus1[0][4].set_color(RED)
        konkretnyVzorecLFminus1[0][5].set_color(RED)
        konkretnyVzorecLFminus1[0][6].set_color(RED)

        konkretnyGrafLFminus2 = suradnicovaOs.plot(lambda y: -2*y+0, x_range=[-4,4])
        konkretnyVzorecLFminus2 = MathTex('{f: y = -2x+0}', font_size=50).to_edge(UL).set_color(YELLOW)
        bod1Minus2= Dot(suradnicovaOs.coords_to_point(-1,2), color=YELLOW)
        bodkociarka1Minus2 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(-1,2))
        bod2Minus2= Dot(suradnicovaOs.coords_to_point(1,-2), color=YELLOW)
        bodkociarka2Minus2 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(1,-2))
        konkretnyVzorecLFminus2[0][4].set_color(RED)
        konkretnyVzorecLFminus2[0][5].set_color(RED)
        konkretnyVzorecLFminus2[0][6].set_color(RED)

        konkretnyGrafLFminus3 = suradnicovaOs.plot(lambda y: -3*y+0, x_range=[-4,4])
        konkretnyVzorecLFminus3 = MathTex('{f: y = -3x+0}', font_size=50).to_edge(UL).set_color(YELLOW)
        bod1Minus3= Dot(suradnicovaOs.coords_to_point(-1,3), color=YELLOW)
        bodkociarka1Minus3 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(-1,3))
        bod2Minus3= Dot(suradnicovaOs.coords_to_point(1,-3), color=YELLOW)
        bodkociarka2Minus3 = suradnicovaOs.get_lines_to_point(suradnicovaOs.c2p(1,-3))
        konkretnyVzorecLFminus3[0][4].set_color(RED)
        konkretnyVzorecLFminus3[0][5].set_color(RED)
        konkretnyVzorecLFminus3[0][6].set_color(RED)


        GrafLFnula = suradnicovaOs.plot(lambda y: -3*y-0, x_range=[-4,4])
        Vzorecnula = MathTex('{f: y = -3x-0}', font_size=50).to_edge(UL).set_color(YELLOW)
        Vzorecnula[0][8].set_color(RED)
        BodNulab = Dot(suradnicovaOs.coords_to_point(0,0), color=YELLOW)

        GrafLFminus1b = suradnicovaOs.plot(lambda y: -3*y-1, x_range=[-4,4])
        Vzorecminus1b = MathTex('{f: y = -3x-1}', font_size=50).to_edge(UL).set_color(YELLOW)
        Vzorecminus1b[0][8].set_color(RED)
        Bodminus1b = Dot(suradnicovaOs.coords_to_point(0,-1), color=YELLOW)
      

        GrafLFminus2b = suradnicovaOs.plot(lambda y: -3*y-2, x_range=[-4,4])
        Vzorecminus2b = MathTex('{f: y = -3x-2}', font_size=50).to_edge(UL).set_color(YELLOW)
        Vzorecminus2b[0][8].set_color(RED)
        Bodminus2b = Dot(suradnicovaOs.coords_to_point(0,-2), color=YELLOW)


        GrafLFminus3b = suradnicovaOs.plot(lambda y: -3*y-3, x_range=[-4,4])
        Vzorecminus3b =  MathTex('{f: y = -3x-3}', font_size=50).to_edge(UL).set_color(YELLOW)
        Vzorecminus3b[0][8].set_color(RED)
        Bodminus3b = Dot(suradnicovaOs.coords_to_point(0,-3), color=YELLOW)

        GrafLFplus1b = suradnicovaOs.plot(lambda y: -3*y+1, x_range=[-4,4])
        Vzorecplus1b =  MathTex('{f: y = -3x+1}', font_size=50).to_edge(UL).set_color(YELLOW)
        Vzorecplus1b[0][8].set_color(RED)
        Bodplus1b = Dot(suradnicovaOs.coords_to_point(0,+1), color=YELLOW)


        GrafLFplus2b = suradnicovaOs.plot(lambda y: -3*y+2, x_range=[-4,4])
        Vzorecplus2b =  MathTex('{f: y = -3x+2}', font_size=50).to_edge(UL).set_color(YELLOW)
        Vzorecplus2b[0][8].set_color(RED)
        Bodplus2b = Dot(suradnicovaOs.coords_to_point(0,+2), color=YELLOW)


        GrafLFplus3b = suradnicovaOs.plot(lambda y: -3*y+3, x_range=[-4,4])
        Vzorecplus3b =  MathTex('{f: y = -3x+3}', font_size=50).to_edge(UL).set_color(YELLOW)
        Vzorecplus3b[0][8].set_color(RED)
        Bodplus3b = Dot(suradnicovaOs.coords_to_point(0,+3), color=YELLOW)






        

        y_label = suradnicovaOs.get_y_axis_label("y").next_to(UP*3.6, RIGHT*1.6)
        x_label = suradnicovaOs.get_x_axis_label("x").next_to(suradnicovaOs)
        grid_labels = VGroup(x_label, y_label)

       # self.play(*[FadeOut(mobj) for mobj in self.mobjects])  vsetky veci co som urobil z obrazovky zmiznu

    
        self.play(Write(text1))
        self.play(Unwrite(text1))                                                             
        self.play(Write(suradnicovaOs), run_time=3)  
        self.play(FadeIn(grid_labels))                                                  
                                                                     
        
        self.play(Create(rastucaLF))  
        self.play(Create(boxLinFunkcie))                                                            
        self.wait()
       
        
        self.play(FadeIn(arrows))
        self.play(Create(cislaab))
        self.wait()

    
        self.play(FadeOut(boxLinFunkcie,arrows, cislaab))
        self.play(Write(arrow3))
  
        
       
        self.play(Write(text2))
        self.play(FadeOut(text2))
        

        #alwaysRedraw
        self.play(Write(konstantnaLFVzorecText))
        
        self.play(ReplacementTransform(rastucaLF,konkretnyVzorecLFnula ))
        self.play(FadeIn(bodNula1, bodNula2))
        self.play(Create(konkretnyGrafLFnula))
        
        #bod nula
        self.play(FadeTransformPieces(konstantnaLFVzorecText, rastucaLFVzorecText))
        self.play(ReplacementTransform(konkretnyVzorecLFnula,konkretnyVzorecLFplus1 ))
        self.play(FadeOut(bodNula1, bodNula2))

        #bod plus1
        self.play(FadeIn(bod1Plus1, bod2Plus1, bodkociarka1Plus1, bodkociarka2Plus1))
        self.play(ReplacementTransform(konkretnyGrafLFnula, konkretnyGrafLFplus1))
        self.play(ReplacementTransform(konkretnyVzorecLFplus1,konkretnyVzorecLFplus2 ))
        self.play(FadeOut(bod1Plus1, bod2Plus1, bodkociarka1Plus1, bodkociarka2Plus1))

        #bod plus 2
        self.play(FadeIn(bod1Plus2, bod2Plus2, bodkociarka1Plus2, bodkociarka2Plus2))
        self.play(ReplacementTransform(konkretnyGrafLFplus1, konkretnyGrafLFplus2 ))
        self.play(FadeOut(bod1Plus2, bod2Plus2, bodkociarka1Plus2, bodkociarka2Plus2))

        #bod plus 3
        self.play(FadeIn(bod1Plus3, bod2Plus3, bodkociarka1Plus3, bodkociarka2Plus3))
        self.play(ReplacementTransform(konkretnyGrafLFplus2, konkretnyGrafLFplus3 ))
        self.play(ReplacementTransform(konkretnyVzorecLFplus2,konkretnyVzorecLFplus3 ))
        self.play(FadeOut(bod1Plus3, bod2Plus3, bodkociarka1Plus3, bodkociarka2Plus3))

       

        #bod minus 1
        self.play(FadeTransformPieces(rastucaLFVzorecText, klesajucaVzorecText))
        self.play(ReplacementTransform(konkretnyVzorecLFplus3,konkretnyVzorecLFminus1 ))
        self.play(FadeIn(bod1Minus1, bod2Minus1, bodkociarka1Minus1, bodkociarka2Minus1))
        self.play(ReplacementTransform(konkretnyGrafLFplus3, konkretnyGrafLFminus1 ))
        self.play(FadeOut(bod1Minus1, bod2Minus1, bodkociarka1Minus1, bodkociarka2Minus1))


        self.play(ReplacementTransform(konkretnyVzorecLFminus1,konkretnyVzorecLFminus2 ))
        self.play(FadeIn(bod1Minus2, bod2Minus2, bodkociarka1Minus2, bodkociarka2Minus2))
        self.play(ReplacementTransform(konkretnyGrafLFminus1, konkretnyGrafLFminus2 ))
        self.play(FadeOut(bod1Minus2, bod2Minus2, bodkociarka1Minus2, bodkociarka2Minus2))


        self.play(ReplacementTransform(konkretnyVzorecLFminus2,konkretnyVzorecLFminus3 ))
        self.play(FadeIn(bod1Minus3, bod2Minus3, bodkociarka1Minus3, bodkociarka2Minus3))
        self.play(ReplacementTransform(konkretnyGrafLFminus2, konkretnyGrafLFminus3 ))
        self.play(FadeOut(bod1Minus3, bod2Minus3, bodkociarka1Minus3, bodkociarka2Minus3))

        self.play(FadeOut(arrow3, klesajucaVzorecText))

        self.play(FadeIn(BodNulab))
        self.play(ReplacementTransform(konkretnyVzorecLFminus3, Vzorecnula))
        self.play(ReplacementTransform(konkretnyGrafLFminus3, GrafLFnula))

        self.play(ReplacementTransform(BodNulab, Bodminus1b))
        self.play(ReplacementTransform(Vzorecnula, Vzorecminus1b))
        self.play(ReplacementTransform(GrafLFnula, GrafLFminus1b))

        self.play(ReplacementTransform(Bodminus1b, Bodminus2b))
        self.play(ReplacementTransform(Vzorecminus1b, Vzorecminus2b))
        self.play(ReplacementTransform(GrafLFminus1b, GrafLFminus2b))

        self.play(ReplacementTransform(Bodminus2b, Bodminus3b))
        self.play(ReplacementTransform(Vzorecminus2b, Vzorecminus3b))
        self.play(ReplacementTransform(GrafLFminus2b, GrafLFminus3b))


        self.play(ReplacementTransform(Bodminus3b, Bodplus1b))
        self.play(ReplacementTransform(Vzorecminus3b, Vzorecplus1b))
        self.play(ReplacementTransform(GrafLFminus3b, GrafLFplus1b))


        self.play(ReplacementTransform(Bodplus1b, Bodplus2b))
        self.play(ReplacementTransform(Vzorecplus1b, Vzorecplus2b))
        self.play(ReplacementTransform(GrafLFplus1b, GrafLFplus2b))

        self.play(ReplacementTransform(Bodplus2b, Bodplus3b))
        self.play(ReplacementTransform(Vzorecplus2b, Vzorecplus3b))
        self.play(ReplacementTransform(GrafLFplus2b, GrafLFplus3b))

        self.wait()
      





       
        
       

     
        
                                                                          


        
        
        
        
        
