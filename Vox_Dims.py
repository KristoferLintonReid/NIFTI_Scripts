def Get_Dims(input_path):
    Rs = []
    input_list = []
    input_list += [each for each in os.listdir(input_path) if each.endswith('.nii') or each.endswith('.nii.gz')]
    for i in input_list: 
        img = nib.load(input_path +i)
        A = img.header.get_zooms()
        Rs.append(((A)))
    np.savetxt(input_path + "NiFTI_Voxel_Data.csv", Rs, delimiter=",", fmt='%s') ### will output a csv file contating all the voxel dimensions can change the name in "" if you like 
