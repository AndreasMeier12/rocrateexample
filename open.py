from rocrate.rocrate import ROCrate


def main():
    crate = ROCrate("rocrate.zip")
    entities = [x for x in crate.get_entities()]
    ro_data = entities[1]
    print("done")


if __name__ == '__main__':
    main()
