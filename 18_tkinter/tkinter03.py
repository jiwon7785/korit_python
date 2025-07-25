import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0, column=0, pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

#entry옆에 버튼 하나 만들고 해당 버튼 클릭시
#아이디 출력
#아이디 밑에 비밀번호도 똑같이 만드세요

def dupl_click():
    #실제 서버와 데이터 베이스에 정보를 요청해서
    #비교하는 중복 확인 절차
    if id_entry.get() == "":
        messagebox.showwarning("경고", "아이디를 입력해주세요.")
    else:
        messagebox.showinfo("중복확인", id_entry.get())

dupl_btn = tk.Button(root, text="중복확인", command=dupl_click)
dupl_btn.grid(row=0, column=2)

password_label = tk.Label(root, text="비밀번호: ")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5)

passcheck_label = tk.Label(root, text="비밀번호 확인: ")
passcheck_label.grid(row=2, column=0)

passcheck_entry = tk.Entry(root, show="*")
passcheck_entry.grid(row=2, column=1, padx=5)

chk_var = tk.IntVar()
chk_box = tk.Checkbutton(root, text="약관 내용에 동의합니다.", variable=chk_var)
chk_box.grid(row=3, column=1)

def signup_click():
    if password_entry.get() != passcheck_entry.get():
        messagebox.showerror("경고", "비밀번호가 일치하지 않습니다.")
    elif chk_var.get() != 1:
        messagebox.showerror("경고", "약관 내용에 동의해야만 가입할 수 있습니다.")
    else:
        messagebox.showinfo("회원가입", "성공적으로 회원가입되었습니다.")

signup_btn = tk.Button(root, text="회원가입")
signup_btn.grid(row=4, column=2)

# 아이디 눌러졌고 비번 눌러졌고 비번과 비번 확인이 일치하고 약관을 동의한 채로 회원가입을 눌렀다면 회원가입이 완료되었습니다 창 띄우기



root.mainloop()