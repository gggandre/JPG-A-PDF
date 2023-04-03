import os
from PIL import Image


def convert_images_to_pdf(folder_path):
    """
    It takes a folder path as input, finds all the .jpg files in the subfolders of that folder, and then
    creates a PDF file with all those images
    
    :param folder_path: The path to the folder containing the subfolders with the images
    :return: the path to the PDF file.
    """
    images = [os.path.join(folder_path, subfolder, f) for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder)) for f in os.listdir(os.path.join(folder_path, subfolder)) if f.endswith('.jpg')]

    if not images:
        print("No se encontraron imágenes .jpg en las subcarpetas de la carpeta especificada")
        return

    images.sort()
    pdf_path = os.path.join(folder_path, "images.pdf")

    with Image.open(images[0]) as img:
        img.save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=[Image.open(image) for image in images[1:]])

    print("El archivo PDF ha sido creado exitosamente")


if __name__ == '__main__':
    folder_path = "Tomos/13"
    convert_images_to_pdf(folder_path)
