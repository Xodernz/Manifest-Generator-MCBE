import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import uuid
#orang impor


# MAIN FUNCTION
def mainFunc():
    packName = "Undefined"
    packDescr = ""
    packType = ""
    
    if manName.get():
        packName = manName.get()
    if manDesc.get():
        packDescr = manDesc.get()
    if selected_dropdown.get() == "Resource Pack":
        packType = "resources"
    elif selected_dropdown.get() == "Behavior Pack":
        packType = "data"
    else:
        resultLabel.config(text="please select pack type!", fg="#FF0000")
        return
    
    saveDir = filedialog.asksaveasfilename(
        title="Simpan sebagai...",
        defaultextension=".json",
        initialfile="manifest.json",
        filetypes=[("Manifest JSON", "*.json")],
        initialdir="./"
    )

    if not saveDir:
        resultLabel.config(text="Cancelled!", fg="#FF0000")
        return

    with open(saveDir, "w") as f:
        f.write(f'{"{"}\n  "format_version": 2,\n  "header": {"{"}\n    "name": "{packName}",\n    "description": "{packDescr}",\n    "uuid": "{uuid.uuid4()}",\n    "version": [1, 0, 0],\n    "min_engine_version": [1, 17, 0]\n  {"}"},\n  "modules": [\n    {"{"}\n      "type": "{packType}",\n      "uuid": "{uuid.uuid4()}",\n      "version": [1, 0, 0]\n    {"}"}\n  ]\n{"}"}')
        resultLabel.config(text="Done...!!!", fg="#009900")




# Main Interface
root = tk.Tk()
root.title("P3 Manifest Generator")

mainGrup = tk.Frame(root)
mainGrup.pack(pady=(10, 0), fill="x", padx=40)

mainGrup.grid_columnconfigure(0, weight=0)

mainGrup.grid_columnconfigure(1, weight=1)


# ROW 0 (Pack Name)
tk.Label(mainGrup, text="Name: ").grid(row=0, column=0, sticky="w", pady=10)
manName = tk.Entry(mainGrup) # Entry (manName)
manName.grid(row=0, column=1, sticky="ew", pady=10)

# ROW 1 (Pack Description)
tk.Label(mainGrup, text="Description: ").grid(row=1, column=0, sticky="w", pady=(0, 10))
manDesc = tk.Entry(mainGrup) # Entry (manDesc)
manDesc.grid(row=1, column=1, sticky="ew", pady=(0, 10))

# ROW 2 (Pack Type Dropdown)
selected_dropdown = tk.StringVar()
tk.Label(mainGrup, text="Pack Type: ").grid(row=2, column=0, sticky="w")
type_pack = ttk.Combobox(mainGrup, textvariable=selected_dropdown, state="readonly")
type_pack["values"] = ("Resource Pack", "Behavior Pack")
type_pack.set("Select Pack Type")
type_pack.grid(row=2, column=1, sticky="ew")


resultLabel = tk.Label(root, text="")
resultLabel.pack(pady=(15, 0))

tk.Button(root, text="Generate", command=mainFunc).pack(pady=(15, 30))

root.update_idletasks()
windowHeight = root.winfo_reqheight()
root.geometry(f"400x{windowHeight}")
root.resizable(False, False)

root.mainloop()
