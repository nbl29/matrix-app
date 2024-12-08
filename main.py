import numpy as np
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

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
        self.layout.add_widget(Label(text="Masukkan Matriks A"))
        self.matrix_a_input = TextInput(hint_text="Contoh: 1,2;3,4", multiline=True)
        self.layout.add_widget(self.matrix_a_input)

        self.layout.add_widget(Label(text="Masukkan Matriks B"))
        self.matrix_b_input = TextInput(hint_text="Contoh: 5,6;7,8", multiline=True)
        self.layout.add_widget(self.matrix_b_input)

        submit_button = Button(text="Submit", on_press=self.submit_matrices)
        self.layout.add_widget(submit_button)

    def submit_matrices(self, instance):
        try:
            a_str = self.matrix_a_input.text.strip()
            b_str = self.matrix_b_input.text.strip()

            self.matrix_a = np.array([[float(num) for num in row.split(',')] for row in a_str.split(';')])
            self.matrix_b = np.array([[float(num) for num in row.split(',')] for row in b_str.split(';')])

            self.display_popup("Success", "Matriks A dan B berhasil dimasukkan!")
        except Exception as e:
            self.display_popup("Error", f"Input tidak valid: {e}")

    def show_matrices(self, instance):
        if self.matrix_a is not None and self.matrix_b is not None:
            self.display_popup("Matriks", f"A:\n{self.matrix_a}\n\nB:\n{self.matrix_b}")
        else:
            self.display_popup("Error", "Matriks belum diinput!")

    def add_matrices(self, instance):
        try:
            result = self.matrix_a + self.matrix_b
            self.display_popup("Hasil A + B", str(result))
        except ValueError:
            self.display_popup("Error", "Dimensi matriks harus sama!")

    def subtract_matrices(self, instance):
        try:
            result = self.matrix_a - self.matrix_b
            self.display_popup("Hasil A - B", str(result))
        except ValueError:
            self.display_popup("Error", "Dimensi matriks harus sama!")

    def multiply_matrices(self, instance):
        try:
            result = np.dot(self.matrix_a, self.matrix_b)
            self.display_popup("Hasil A × B", str(result))
        except ValueError:
            self.display_popup("Error", "Dimensi matriks tidak sesuai untuk perkalian!")

    def transpose_matrices(self, instance):
        transposed_a = self.matrix_a.T
        transposed_b = self.matrix_b.T
        self.display_popup("Transpose Matriks", f"A^T:\n{transposed_a}\n\nB^T:\n{transposed_b}")

    def calculate_determinant(self, instance):
        det_a = hitung_determinan(self.matrix_a)
        det_b = hitung_determinan(self.matrix_b)
        self.display_popup("Determinan Matriks", f"Determinan A: {det_a}\nDeterminan B: {det_b}")

    def solve_linear_system(self, instance):
        try:
            b = self.matrix_b.flatten()
            solusi = solve_sistem_persamaan(self.matrix_a, b)
            self.display_popup("Solusi SPL", f"Solusi: {solusi}")
        except Exception as e:
            self.display_popup("Error", f"Gagal menyelesaikan SPL: {e}")

    def display_popup(self, title, content):
        content_label = Label(text=content, size_hint_y=None)
        content_label.bind(texture_size=lambda instance, size: setattr(instance, 'height', size[1]))
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 200))
        scroll_view.add_widget(content_label)

        popup = Popup(title=title, content=scroll_view, size_hint=(None, None), size=(400, 300))
        popup.open()

    def stop(self, instance):
        App.get_running_app().stop()

if __name__ == "__main__":
    MatrixApp().run()
