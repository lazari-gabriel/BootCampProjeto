import customtkinter as ctk

# Lista de fontes (a sua lista original)
fontes = [
    "@MS Gothic", "@MS PGothic", "@MS UI Gothic", "@Malgun Gothic", "@Malgun Gothic Semilight",
    "@Microsoft JhengHei", "@Microsoft JhengHei Light", "@Microsoft JhengHei UI", "@Microsoft JhengHei UI Light",
    "@Microsoft YaHei", "@Microsoft YaHei Light", "@Microsoft YaHei UI", "@Microsoft YaHei UI Light",
    "@MingLiU-ExtB", "@MingLiU_HKSCS-ExtB", "@NSimSun", "@PMingLiU-ExtB", "@SimSun", "@SimSun-ExtB", "@SimSun-ExtG",
    "@Yu Gothic", "@Yu Gothic Light", "@Yu Gothic Medium", "@Yu Gothic UI", "@Yu Gothic UI Light",
    "@Yu Gothic UI Semibold", "@Yu Gothic UI Semilight", "Arabic Transparent", "Arial", "Arial Baltic",
    "Arial Black", "Arial CE", "Arial CYR", "Arial Greek", "Arial TUR", "Bahnschrift", "Bahnschrift Condensed",
    "Bahnschrift Light", "Bahnschrift Light Condensed", "Bahnschrift Light SemiCondensed",
    "Bahnschrift SemiBold", "Bahnschrift SemiBold Condensed", "Bahnschrift SemiBold SemiConden",
    "Bahnschrift SemiCondensed", "Bahnschrift SemiLight", "Bahnschrift SemiLight Condensed",
    "Bahnschrift SemiLight SemiConde", "Calibri", "Calibri Light", "Cambria", "Cambria Math",
    "Candara", "Candara Light", "Comic Sans MS", "Consolas", "Constantia", "Corbel", "Corbel Light",
    "Courier", "Courier New", "Courier New Baltic", "Courier New CE", "Courier New CYR", "Courier New Greek",
    "Courier New TUR", "Ebrima", "El&Font Bubble", "Fixedsys", "Franklin Gothic Medium", "Gabriola",
    "Gadugi", "Georgia", "HoloLens MDL2 Assets", "Impact", "Ink Free", "Javanese Text", "Jungle LIFE",
    "Leelawadee UI", "Leelawadee UI Semilight", "Lucida Console", "Lucida Sans Unicode",
    "MS Gothic", "MS PGothic", "MS Sans Serif", "MS Serif", "MS UI Gothic", "MV Boli", "Malgun Gothic",
    "Malgun Gothic Semilight", "Marlett", "Metropolis Light", "Microsoft Himalaya", "Microsoft JhengHei",
    "Microsoft JhengHei Light", "Microsoft JhengHei UI", "Microsoft JhengHei UI Light",
    "Microsoft New Tai Lue", "Microsoft PhagsPa", "Microsoft Sans Serif", "Microsoft Tai Le",
    "Microsoft YaHei", "Microsoft YaHei Light", "Microsoft YaHei UI", "Microsoft YaHei UI Light",
    "Microsoft Yi Baiti", "MingLiU-ExtB", "MingLiU_HKSCS-ExtB", "Modern", "Mongolian Baiti",
    "Myanmar Text", "NSimSun", "Neo Sans", "Nirmala UI", "Nirmala UI Semilight", "PMingLiU-ExtB",
    "Palatino Linotype", "Roading Night", "Roman", "Script", "Segoe MDL2 Assets", "Segoe Print",
    "Segoe Script", "Segoe UI", "Segoe UI Black", "Segoe UI Emoji", "Segoe UI Historic", "Segoe UI Light",
    "Segoe UI Semibold", "Segoe UI Semilight", "Segoe UI Symbol", "SimSun", "SimSun-ExtB", "SimSun-ExtG",
    "Sitka Banner", "Sitka Display", "Sitka Heading", "Sitka Small", "Sitka Subheading", "Sitka Text",
    "Small Fonts", "Sylfaen", "Symbol", "System", "Tahoma", "Terminal", "Times New Roman",
    "Times New Roman Baltic", "Times New Roman CE", "Times New Roman CYR", "Times New Roman Greek",
    "Times New Roman TUR", "Trebuchet MS", "Verdana", "Webdings", "Wingdings", "Yu Gothic",
    "Yu Gothic Light", "Yu Gothic Medium", "Yu Gothic UI", "Yu Gothic UI Light",
    "Yu Gothic UI Semibold", "Yu Gothic UI Semilight"
]


ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("Visualizador de Fontes")
root.geometry("500x600")

scroll_frame = ctk.CTkScrollableFrame(root, width=480, height=580)
scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

for f in fontes:
    try:
        lbl = ctk.CTkLabel(scroll_frame, text=f"Fonte: {f}", font=(f, 16))
        lbl.pack(anchor="w", padx=5, pady=2)
    except Exception:
        lbl = ctk.CTkLabel(scroll_frame, text=f"[NÃO DISPONÍVEL] {f}", font=("Arial", 12), text_color="red")
        lbl.pack(anchor="w", padx=5, pady=2)

root.mainloop()
