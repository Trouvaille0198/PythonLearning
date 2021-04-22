import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from client import Client
import socket


class ClientGUI():
    def __init__(self, master):
        self.root = master
        self.root.title('Client')
        self.root.geometry('600x600')
        self.client = 1
        # MainPage(self.root)
        ConnectPage(self.root)


class MainPage():
    def __init__(self, master):
        self.master = master
        self.main_page = tk.Frame(self.master)
        self.main_page.grid()
        self.msg_button = tk.Button(self.main_page,
                                    text='send',
                                    command=self.send_msg).grid(row=0,
                                                                column=0)
        self.exit_button = tk.Button(self.main_page,
                                     text='exit',
                                     state='disabled').grid(row=1, column=0)


class ConnectPage():
    def __init__(self, master):
        self.master = master
        self.connect_page = tk.Frame(self.master)
        self.connect_page.grid()

        tk.Label(self.connect_page, text="ip ").grid(row=0)
        self.ip_entry = tk.Entry(self.connect_page)
        self.ip_entry.grid(row=0, column=1)
        tk.Label(self.connect_page, text="port ").grid(row=1)
        self.port_entry = tk.Entry(self.connect_page)
        self.port_entry.grid(row=1, column=1)
        self.connect_btn = tk.Button(self.connect_page,
                                     text='connect',
                                     command=self.connect).grid(row=3)

    def connect(self):
        ip = self.ip_entry.get() if self.ip_entry.get(
        ) else socket.gethostname()
        port = int(self.port_entry.get()) if self.port_entry.get() else 5000
        global client
        client = Client(ip, port)
        is_connected = client.connect()
        if is_connected == True:
            self.connect_page.destroy()
            LoginPage(self.master)
        else:
            messagebox.showerror("Python Demo", "connection failed!")


class LoginPage():
    def __init__(self, master):
        self.master = master
        self.login_page = tk.Frame(self.master)
        self.login_page.grid()

        tk.Label(self.login_page, text='username').grid(row=0)
        self.user_entry = tk.Entry(self.login_page)
        self.user_entry.grid(row=0, column=1)
        tk.Label(self.login_page, text='password').grid(row=1)
        self.passwrd_entry = tk.Entry(self.login_page)
        self.passwrd_entry.grid(row=1, column=1)

        self.login_btn = tk.Button(self.login_page,
                                   text='login',
                                   command=self.login).grid(row=3)

    def login(self):
        username = self.user_entry.get()
        password = self.passwrd_entry.get()
        res = client.login(username, password)
        if res == 'Login successfully!':
            messagebox.showinfo("Python Demo", "login successfully!")
            self.login_page.destroy()
            MainPage(self.master)
        else:
            messagebox.showerror("Python Demo", "login failed!")