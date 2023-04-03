import os
from PIL import Image


def convert_images_to_pdf(folder_path):
    """
    It takes a folder path, looks for all the .jpg files in the
    subfolders of that folder, and then
    creates a PDF file with all those images
    :param folder_path: The path to the folder containing the images
    :return: the path of the PDF file that was created.
    """
    images = []
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            for f in os.listdir(subfolder_path):
                if f.endswith('.jpg'):
                    image_path = os.path.join(subfolder_path, f)
                    try:
                        with Image.open(image_path) as img:
                            img.load()  # Cargar la imagen para verificar si
                            # está completa
                        images.append(image_path)
                    except Exception as e:
                        print(f"Error al cargar la imagen {image_path}: {e}")

    if not images:
        print("No se encontraron imágenes .jpg en el directorio")

    images.sort()
    pdf_path = os.path.join(folder_path, "images.pdf")

    with Image.open(images[0]) as img:
        img.save(pdf_path, "PDF", resolution=100.0, save_all=True,
                 append_images=[Image.open(image).convert('RGB')
                                for image in images[1:]])

    print("El archivo PDF ha sido creado exitosamente")


if __name__ == '__main__':
    folder_path = "Tomos/17"
    convert_images_to_pdf(folder_path)
