import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

root = tk.Tk()
root.title("Co-LIFE")
root.config(bg="#40E0D0")

#görevlerin eklendiği liste
missions = []

#görev adının girildiği entry
mission_entry = tk.Entry(root, width=30, bg="#32405b", fg="white")
mission_entry.grid(row=0, column=0, padx=5, pady=5)

#görev başlangıç tarihi için entry alanı
start_label = tk.Label(root, text="Başlama Tarihi (YYYY-MM-DD):", bg="#32405b", fg="white")
start_label.grid(row=1, column=0, padx=5, pady=5)
start_entry = tk.Entry(root, width=15, bg="#32405b", fg="white")
start_entry.grid(row=1, column=1, padx=5, pady=5)

#görev bitiş tarihi için entry alanı
end_label = tk.Label(root, text="Bitiş Tarihi (YYYY-MM-DD):", bg="#32405b", fg="white")
end_label.grid(row=1, column=2, padx=5, pady=5)
end_entry = tk.Entry(root, width=15, bg="#32405b", fg="white")
end_entry.grid(row=1, column=3, padx=5, pady=5)

#görevleri gösteren tablo için
mission_table = ttk.Treeview(root, columns=("Task", "Start Date", "End Date", "Completed"), show="headings", selectmode="browse")
mission_table.heading("Task", text="Görev")
mission_table.heading("Start Date", text="Başlama Tarihi")
mission_table.heading("End Date", text="Bitiş Tarihi")
mission_table.heading("Completed", text="Tamamlandı")
mission_table.column("Task", width=200, anchor="center")
mission_table.column("Start Date", width=100, anchor="center")
mission_table.column("End Date", width=100, anchor="center")
mission_table.column("Completed", width=80, anchor="center")
mission_table.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

#görev ekleme fonksiyonu
def mission_add():
    mission_text = mission_entry.get().strip()
    start = start_entry.get().strip()
    end = end_entry.get().strip()

    #görev adı,başlangıç ve bitiş tarihi girilmediği takdirde hata veren messagebox
    if not mission_text or not start or not end:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
        return
    #geçerli tarih girilmediği takdirde hata fırlatmak için
    try:
        start = datetime.strptime(start, "%Y-%m-%d").date()
        end = datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz tarih formatı. (YYYY-MM-DD)")
        return
    #görev başlangıç tarihi bitiş tarihinden önce olursa gösterilen messagebox
    if start > end:
        messagebox.showerror("Hata", "Başlama tarihi, bitiş tarihinden sonra olamaz.")
        return

    #görevler için sözlük oluşturup listeye ekleme
    mission = {"task_text": mission_text, "start_date": start, "end_date": end, "completed": False}
    missions.append(mission)
    table_revise()
    entry_clean()
    mission_write()

#görev tamamlama komutu için fonksiyon
def mission_done():
    selected_task_index = mission_table.selection()
    if selected_task_index:
        task_index = int(mission_table.index(selected_task_index))
        missions[task_index]["completed"] = True
        table_revise()
        mission_write()

#görev silmek için fonksiyon
def mission_delete():
    selected_task_index = mission_table.selection()
    if selected_task_index:
        task_index = int(mission_table.index(selected_task_index))
        mission_table.delete(selected_task_index)
        if task_index < len(missions):
            entry_clean = missions.pop(task_index)
            mission_write()

#görevleri bitiş tarihine göre sıralamak için fonksiyon
def mission_sort():
    missions.sort(key=lambda x: x["end_date"])
    table_revise()
    mission_write()

#görev girilen entry'leri temizleyen fonksiyon
def entry_clean():
    mission_entry.delete(0, tk.END)
    start_entry.delete(0, tk.END)
    end_entry.delete(0, tk.END)

#görev tablosunu güncellemek için fonksiyon
def table_revise():
    for i in mission_table.get_children():
        mission_table.delete(i)

    for task in missions:
        completed_text = "Evet" if task["completed"] else "Hayır"
        mission_table.insert("", "end", values=(task["task_text"], task["start_date"], task["end_date"], completed_text), tags=())

#görev bilgilerini text dosyasına yazdıran fonksiyon
def mission_write():
    with open("gorevler.txt", "w") as file:
        for task in missions:
            file.write(f"{task['task_text']} - Başlama: {task['start_date']} - Bitiş: {task['end_date']} - Tamamlandı: {task['completed']}\n")

#görevleri uygulama açılınca yüklemek için fonksiyon
def mission_load():
    try:
        with open("gorevler.txt", "r") as file:
            task_lines = file.read().splitlines()
            for task_line in task_lines:
                task_data = parse_task_data(task_line)
                if task_data:
                    missions.append(task_data)
    except FileNotFoundError:
        pass

    table_revise()

#görevin verisini ayrıştırarak sözlük oluşturan fonksiyon
def parse_task_data(task_string):
    parts = task_string.split(" - ")
    if len(parts) >= 4:
        task_text = parts[0]
        start_date = datetime.strptime(parts[1].split(": ")[1], "%Y-%m-%d").date()
        end_date = datetime.strptime(parts[2].split(": ")[1], "%Y-%m-%d").date()
        completed = parts[3].split(": ")[1].lower() == 'true'
        return {"task_text": task_text, "start_date": start_date, "end_date": end_date, "completed": completed}
    return None

#görev eklemek için basılan butonu
add_button = tk.Button(root, text="Görev Ekle", command=mission_add, bg="#32405b", fg="white")
add_button.grid(row=2, column=0, columnspan=4, pady=10)

#sıralama yapmak için basılan buton
sort_button = tk.Button(root, text="Bitiş Tarihine Göre Sırala", command=mission_sort, bg="#808080")
sort_button.grid(row=4, column=0, columnspan=4, pady=10)

#görevi tamamlamak için basılan buton
done_button = tk.Button(root, text="Görevi Tamamla", command=mission_done, bg="#008000")
done_button.grid(row=5, column=0, columnspan=4, pady=5)

#görev silmek için basılan buton
delete_button = tk.Button(root, text="Görevi Sil", command=mission_delete, bg="#990000")
delete_button.grid(row=6, column=0, columnspan=4, pady=5)

mission_load()

root.mainloop()
