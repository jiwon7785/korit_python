import tkinter as tk
from tkinter import messagebox, font

#1. 메뉴 정의
menu_items = {
    "아메리카노" : 3000,
    "라떼" : 4000,
    "케이크" : 5000,
    "샌드위치" : 6500,
    "쿠키" : 2000
}

#2. 기본 창 생성
root = tk.Tk()
root.title("메뉴 주문하기")
root.geometry("350x400")
root.resizable(False, False)

#각 메뉴를 선택했을 때 선택 메뉴들을 담아둘 딕셔너리
item_vars = {}

#3. 메뉴 표시
tk.Label(root, text="--- 메뉴를 선택하세요 ---", font=font.Font(size=14, weight="bold")).grid(row=0, column=0, pady=10)

row_num = 1
for item_name, price in menu_items.items():
    item_vars[item_name] = tk.IntVar()

    #체크 박스
    chk = tk.Checkbutton(root, text=item_name, variable=item_vars[item_name], font=font.Font(size=12))
    chk.grid(row=row_num, sticky="w", column=0, padx=20, pady=2)

    #가격 레이블
    price_label = tk.Label(root, text=f"{price}원", font=font.Font(size=12))
    price_label.grid(row=row_num, sticky="e", padx=20, pady=2)



    row_num += 1

def calculate_order():
    selected_order = []
    total_price = 0

    for item_name, var in item_vars.items():
        if var.get() == 1:
            selected_order.append(item_name)
            total_price += menu_items[item_name]

    order_text = "주문 내역:\n"
    if selected_order:
        for item in selected_order:
            order_text += f"- {item}\n"
        order_text += f"\n총 금액: {total_price}원"
        messagebox.showinfo("주문 확인", order_text)
    else:
        messagebox.showwarning("주문 오류", "선택된 메뉴가 없습니다.")

order_btn = tk.Button(root, text="주문하기", command=calculate_order)
order_btn.grid(row=row_num + 1, column=0, columnspan=2, pady=10)

root.mainloop()
