from pathlib import Path
from unstructured.partition.pdf import partition_pdf


def extract_pdf(pdf_path: str):
    elements = partition_pdf(
        filename=pdf_path,
        strategy="hi_res",
        infer_table_structure=True,
        extract_image_block_types=["Image"],
    )
    
    print(elements[0].metadata.to_dict())
    return elements


if __name__ == "__main__":
    pdf_folder = Path("data/raw")

    pdf_files = list(pdf_folder.glob("*.pdf"))

    if not pdf_files:
        print("No PDFs found.")
    else:
        elements = extract_pdf(str(pdf_files[0]))

        # print(f"PDF: {pdf_files[0].name}")
        # print(f"Elements extracted: {len(elements)}")

        for element in elements:
            metadata = element.metadata.to_dict()

            if metadata.get("coordinates"):
                print("=" * 80)

                print("Element Type:")
                print(type(element).__name__)

                print("\nPage Number:")
                print(metadata.get("page_number"))

                print("\nCoordinates:")
                print(metadata["coordinates"])

                print("\nText Preview:")
                print(element.text[:200])

                break