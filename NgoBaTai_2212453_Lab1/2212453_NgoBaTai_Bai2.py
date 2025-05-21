import Bai2.Menu as Menu
import Bai2.chuc_nang as chuc_nang
def chaychuongtrinh():
    while(True):
        chon = Menu.chonmenu(12)
        Menu.xulymenu(chon)
        if(chon==0):
            break

chaychuongtrinh()

