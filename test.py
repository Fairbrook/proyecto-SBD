
if __name__ == "__main__":
    from models.editorial import Editorial
    ed = Editorial('patito', 'mexico')
    # ed.save()

    print(ed.getAll())
