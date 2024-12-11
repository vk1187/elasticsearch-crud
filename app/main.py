from crud_operations import create_index,create_document ,read_document ,update_document , delete_document
# from app.crud_operations import (
#     create_index, create_document, read_document,
#     update_document, delete_document
# )



if __name__ == "__main__":
    # Create an index
    print(create_index())

    # Create a document
    print(create_document("1", {"name": "Amit", "age": 30}))

    # Read a document
    print(read_document("1"))

    # Update a document
    print(update_document("1", {"age": 31}))

    # Delete a document
    print(delete_document("1"))
