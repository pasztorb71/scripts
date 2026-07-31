from akp_authorization import Base
from eralchemy import render_er

if __name__ == "__main__":
    # Az ER diagramot a Base alapján generáljuk
    render_er(Base, "akp_authorization_er_diagram.png")
    print("ER diagram elkészült: akp_authorization_er_diagram.png")

