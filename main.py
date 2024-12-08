import numpy as np
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

def hitung_determinan(matriks):
    """Menghitung determinan matriks"""
    try:
        return round(np.linalg.det(matriks), 4)
    except np.linalg.LinAlgError:
        return "Error: Matriks tidak memiliki determinan"

def solve_sistem_persamaan(A, b):
    """Menyelesaikan sistem persamaan linear Ax = b"""
    try:
        solusi = np.linalg.solve(A, b)
        return solusi
    except np.linalg.LinAlgError:
        return "Error: Sistem persamaan tidak memiliki solusi atau tidak valid"

class MatrixApp(App):
    def build(self):
        self.matrix_a = None
        self.matrix_b = None
        
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.title = Label(text="Program Operasi Matriks", font_size=24, size_hint_y=None, height=40)
        self.layout.add_widget(self.title)

        self.menu_buttons = [
            Button(text="Input Matriks", on_press=self.input_matriks),
            Button(text="Tampilkan Matriks", on_press=self.show_matrices),
            Button(text="Penjumlahan Matriks", on_press=self.add_matrices),
            Button(text="Pengurangan Matriks", on_press=self.subtract_matrices),
            Button(text="Perkalian Matriks", on_press=self.multiply_matrices),
            Button(text="Transpose Matriks", on_press=self.transpose_matrices),
            Button(text="Determinan Matriks", on_press=self.calculate_determinant),
            Button(text="Sistem Persamaan Linear", on_press=self.solve_linear_system),
            Button(text="Keluar", on_press=self.stop)
        ]

        for button in self.menu_buttons:
            self.layout.add_widget(button)
        
        return self.layout

    def clear_layout(self):
        self.layout.clear_widgets()
        self.layout.add_widget(self.title)
        for button in self.menu_buttons:
            self.layout.add_widget(button)
    
    def input_matriks(self, instance):
        self.clear_layout()
        self.layout.add_widget(Label(text="Input Matriks A"))
        self.matrix_a_input = GridLayout(cols=2, rows=2, size_hint_y=None, height=40)
        self.matrix_a_input.add_widget(Label(text="Baris A:"))
        self.matrix_a_rows = TextInput(hint_text="Enter Rows", multiline=False)
        self.matrix_a_input.add_widget(self.matrix_a_rows)
        self.layout.add_widget(self.matrix_a_input)

        self.layout.add_widget(Label(text="Input Matriks B"))
        self.matrix_b_input = GridLayout(cols=2, rows=2, size_hint_y=None, height=40)
        self.matrix_b_input.add_widget(Label(text="Baris B:"))
        self.matrix_b_rows = TextInput(hint_text="Enter Rows", multiline=False)
        self.matrix_b_input.add_widget(self.matrix_b_rows)
        self.layout.add_widget(self.matrix_b_input)

        submit_button = Button(text="Submit", on_press=self.submit_matrices)
        self.layout.add_widget(submit_button)

    def submit_matrices(self, instance):
        try:
            a_rows = int(self.matrix_a_rows.text)
            b_rows = int(self.matrix_b_rows.text)
            self.matrix_a = np.random.rand(a_rows, a_rows)
            self.matrix_b = np.random.rand(b_rows, b_rows)
            self.display_popup("Success", f"Matriks A dan B berhasil dimasukkan!")
        except ValueError:
            self.display_popup("Error", "Masukkan jumlah baris yang valid!")

    def show_matrices(self, instance):
        if self.matrix_a is not None and self.matrix_b is not None:
            matrix_a_str = f"A: {self.matrix_a}"
            matrix_b_str = f"B: {self.matrix_b}"
            self.display_popup("Matriks", matrix_a_str + "\n" + matrix_b_str)
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def add_matrices(self, instance):
        if self.matrix_a is not None and self.matrix_b is not None:
            try:
                result = self.matrix_a + self.matrix_b
                self.display_popup("Hasil A + B", str(result))
            except ValueError:
                self.display_popup("Error", "Dimensi matriks harus sama!")
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def subtract_matrices(self, instance):
        if self.matrix_a is not None and self.matrix_b is not None:
            try:
                result = self.matrix_a - self.matrix_b
                self.display_popup("Hasil A - B", str(result))
            except ValueError:
                self.display_popup("Error", "Dimensi matriks harus sama!")
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def multiply_matrices(self, instance):
        if self.matrix_a is not None and self.matrix_b is not None:
            try:
                result = np.dot(self.matrix_a, self.matrix_b)
                self.display_popup("Hasil A × B", str(result))
            except ValueError:
                self.display_popup("Error", "Dimensi matriks tidak sesuai untuk perkalian!")
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def transpose_matrices(self, instance):
        if self.matrix_a is not None and self.matrix_b is not None:
            transposed_a = self.matrix_a.T
            transposed_b = self.matrix_b.T
            self.display_popup("Transpose Matriks", f"A^T:\n{transposed_a}\nB^T:\n{transposed_b}")
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def calculate_determinant(self, instance):
        if self.matrix_a is not None:
            det_a = hitung_determinan(self.matrix_a)
            det_b = hitung_determinan(self.matrix_b) if self.matrix_b is not None else None
            result = f"Determinan A: {det_a}\nDeterminan B: {det_b}" if det_b else f"Determinan A: {det_a}"
            self.display_popup("Determinan Matriks", result)
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def solve_linear_system(self, instance):
        if self.matrix_a is not None:
            # Implement the solver here if needed
            pass
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def display_popup(self, title, content):
        content_label = Label(text=content)
        popup = Popup(title=title, content=content_label, size_hint=(None, None), size=(400, 200))
        popup.open()

    def stop(self, instance):
        self.stop()

if __name__ == "__main__":
    app = MatrixApp()
    app.run()