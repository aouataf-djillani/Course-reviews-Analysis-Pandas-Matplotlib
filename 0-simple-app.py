import justpy as jp
def app():
    wp=jp.QuasarPage()
    #heading 
    h1=jp.QDiv(a=wp, text="Analysis of Course reviews", classes= "text-h3 text-center q-pb-md" )
    p1=jp.QDiv(a=wp, text="These graphs represent course review analysis")

    return wp  

jp.justpy(app)

