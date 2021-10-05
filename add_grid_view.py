import os
import mobie


def add_grid(view_name = "grid1",
             source_names = [["SM_02_Grid2_c264"],
                                  ["SM_02_Grid2_c222"],
                                  ["SM_02_Grid2_c141"],
                                  ["SM_01_Grid5_c166"]],
             dataset = "./data/tomo"
             ):
    """Add a grid view using the 'grid' sourceTransform.
    """
    
    # make sure that the table is not there, otherwise this creates issues
    table_path = f"./data/tomo/tables/{view_name}/default.tsv"
    if os.path.exists(table_path):
        os.remove(table_path)

    view = mobie.metadata.get_grid_view(
        dataset,
        view_name,
        source_names,
        center_at_origin=True
    )
    mobie.validation.validate_view_metadata(view)
    mobie.metadata.add_view_to_dataset("./data/tomo", view_name, view, overwrite=True)


def add_trafo_grid(view_name = "grid1",
             source_names = [["SM_02_Grid2_c264"],
                                  ["SM_02_Grid2_c222"],
                                  ["SM_02_Grid2_c141"],
                                  ["SM_01_Grid5_c166"]],
             dataset = "./data/tomo"
             ):
    """Add a grid view using the 'transformGrid' sourceTransform.
    """
    
    
      
    view_name = "B-ALL-tomos"
    
    
    source_names=[['B-ALL_00_Grid5_c0008'],
                  ['B-ALL_00_Grid5_c0011'],
                  ['B-ALL_00_Grid5_c0043'],
                  ['B-ALL_00_Grid5_c0064'],
                  ['B-ALL_00_Grid5_c0083'],
                  ['B-ALL_00_Grid5_c0103'],
                  ['B-ALL_00_Grid5_c0116'],
                  ['B-ALL_00_Grid5_c0192'],
                  ['B-ALL_00_Grid5_c0212'],
                  ['B-ALL_00_Grid5_c0223'],
                  ['B-ALL_00_Grid5_c0250'],
                  ['B-ALL_00_Grid5_c0283'],
                  ['B-ALL_00_Grid5_c0321'],
                  ['B-ALL_00_Grid5_c0328'],
                  ['B-ALL_00_Grid5_c0330'],
                  ['B-ALL_00_Grid5_c0358'],
                  ['B-ALL_00_Grid5_c0359'],
                  ['B-ALL_00_Grid5_c0363'],
                  ['B-ALL_00_Grid5_c0423'],
                  ['B-ALL_00_Grid5_c0478'],
                  ['B-ALL_00_Grid5_c0484'],
                  ['B-ALL_00_Grid5_c0507'],
                  ['B-ALL_00_Grid5_c0509'],
                  ['B-ALL_00_Grid5_c0526'],
                  ['B-ALL_00_Grid5_c0531'],
                  ['B-ALL_00_Grid5_c0534'],
                  ['B-ALL_00_Grid5_c0573'],
                  ['B-ALL_00_Grid5_c0594'],
                  ['B-ALL_00_Grid5_c0628'],
                  ['B-ALL_00_Grid5_c0630'],
                  ['B-ALL_00_Grid5_c0644'],
                  ['B-ALL_00_Grid5_c0654'],
                  ['B-ALL_00_Grid5_c0707'],
                  ['B-ALL_00_Grid5_c0711'],
                  ['B-ALL_00_Grid5_c0714'],
                  ['B-ALL_00_Grid5_c0732'],
                  ['B-ALL_00_Grid5_c0755'],
                  ['B-ALL_00_Grid5_c0782'],
                  ['B-ALL_00_Grid5_c0783'],
                  ['B-ALL_00_Grid5_c0822'],
                  ['B-ALL_00_Grid5_c0823'],
                  ['B-ALL_00_Grid5_c0843'],
                  ['B-ALL_00_Grid5_c0881'],
                  ['B-ALL_00_Grid5_c0891'],
                  ['B-ALL_00_Grid5_c0930'],
                  ['B-ALL_00_Grid5_c0942'],
                  ['B-ALL_00_Grid5_c0984'],
                  ['B-ALL_00_Grid5_c1020'],
                  ['B-ALL_00_Grid5_c1028'],
                  ['B-ALL_00_Grid5_c1059'],
                  ['B-ALL_00_Grid5_c1062'],
                  ['B-ALL_00_Grid5_c1068'],
                  ['B-ALL_00_Grid5_c1071'],
                  ['B-ALL_00_Grid5_c1131'],
                  ['B-ALL_00_Grid5_c1135'],
                  ['B-ALL_00_Grid5_c1166'],
                  ['B-ALL_00_Grid5_c1173'],
                  ['B-ALL_00_Grid5_c1214'],
                  ['B-ALL_00_Grid5_c1232'],
                  ['B-ALL_00_Grid5_c1336'],
                  ['B-ALL_00_Grid5_c1430'],
                  ['B-ALL_00_Grid5_c1451'],
                  ['B-ALL_00_Grid5_c1525']]
    
    
    # make sure that the table is not there, otherwise this creates issues
    table_path = f"./data/tomo/tables/{view_name}/default.tsv"
    if os.path.exists(table_path):
        os.remove(table_path)

    view = mobie.metadata.get_grid_view(
        dataset,
        view_name,
        source_names,
        use_transform_grid=True,
        center_at_origin=True
    )
    mobie.validation.validate_view_metadata(view)
    mobie.metadata.add_view_to_dataset("./data/tomo", view_name, view, overwrite=True)


def add_mock_crop_grid():
    """Add a grid view using the 'transformGrid' sourceTransform after applying an affine and crop transform.
    """
    view_name = "mock-crop-grid"
    # make sure that the table is not there, otherwise this creates issues
    table_path = f"./data/tomo/tables/{view_name}/default.tsv"
    if os.path.exists(table_path):
        os.remove(table_path)

    source_names = ["SM_02_Grid2_c264", "SM_02_Grid2_c222", "SM_02_Grid2_c141", "SM_01_Grid5_c166"]

    # NOTE: this returns transforms with hard-coded params,
    # substitute with correct computation based on source_name
    def get_affine_and_crop(source_name):
        affine_params = [
            0.9139845918849868, 0.31631199291837175, -0.2541237669578392, 0.0,
            -0.3163119929183716, 0.947725139853161, 0.04199740975719857, 0.0,
            0.2541237669578391, 0.04199740975719859, 0.9662594520318256, 0.0
        ]
        crop_min, crop_max = [1.36, 0.54, 0.27], [2.36, 1.54, 1.27]
        return [
            mobie.metadata.get_affine_source_transform([source_name], affine_params),
            mobie.metadata.get_crop_source_transform([source_name], crop_min, crop_max)
        ]

    additional_source_transforms = [
        trafo for source_name in source_names for trafo in get_affine_and_crop(source_name)
    ]

    view = mobie.metadata.get_grid_view(
        "data/tomo",
        view_name,
        [[source_name] for source_name in source_names],
        use_transform_grid=True,
        center_at_origin=True,
        additional_source_transforms=additional_source_transforms
    )
    mobie.validation.validate_view_metadata(view)
    mobie.metadata.add_view_to_dataset("./data/tomo", view_name, view, overwrite=True)


def add_mock_crop_grid_with_source_name_after_trafo():
    """Add a grid view using the 'transformGrid' sourceTransform after applying an affine and crop transform.
    Using the source_names_after_transform field.

    Note: this is just for demonstration purposes and the 'add_mock_crop_grid' example is preferable in this
    case, as it produces the same result with less complicated code and smaller metadata.
    This feature is only necessary for showing the same source, but transformed differently, in a common view.
    """
    view_name = "mock-crop-grid-trafo-names"
    # make sure that the table is not there, otherwise this creates issues
    table_path = f"./data/tomo/tables/{view_name}/default.tsv"
    if os.path.exists(table_path):
        os.remove(table_path)

    source_names = ["SM_02_Grid2_c264", "SM_02_Grid2_c222", "SM_02_Grid2_c141", "SM_01_Grid5_c166"]

    # NOTE: this returns transforms with hard-coded params,
    # substitute with correct computation based on source_name
    def get_affine_and_crop(source_name):
        affine_params = [
            0.9139845918849868, 0.31631199291837175, -0.2541237669578392, 0.0,
            -0.3163119929183716, 0.947725139853161, 0.04199740975719857, 0.0,
            0.2541237669578391, 0.04199740975719859, 0.9662594520318256, 0.0
        ]
        crop_min, crop_max = [1.36, 0.54, 0.27], [2.36, 1.54, 1.27]
        return [
            mobie.metadata.get_affine_source_transform([source_name], affine_params,
                                                       source_names_after_transform=[source_name + "_aff"]),
            mobie.metadata.get_crop_source_transform([source_name + "_aff"], crop_min, crop_max,
                                                     source_names_after_transform=[source_name + "_cropped"]),
        ]

    additional_source_transforms = [
        trafo for source_name in source_names for trafo in get_affine_and_crop(source_name)
    ]

    view = mobie.metadata.get_grid_view(
        "data/tomo",
        view_name,
        [[source_name] for source_name in source_names],
        use_transform_grid=True,
        center_at_origin=True,
        additional_source_transforms=additional_source_transforms,
        # here, we need to specify the actual sources for the grid transform as a dictionary
        # we need to specify the name of the transformed source for the grid, i.e. <SOURCE_NAME>_cropped
        grid_sources=[[source_name + "_cropped"] for source_name in source_names]
    )
    mobie.validation.validate_view_metadata(view)
    mobie.metadata.add_view_to_dataset("./data/tomo", view_name, view, overwrite=True)




def add_crop_grid(source_names = ["SM_02_Grid2_c264"+ '_c1_crop',
                                  "SM_02_Grid2_c222"+ '_c1_crop',
                                  "SM_02_Grid2_c141"+ '_c1_crop',
                                  "SM_01_Grid5_c166"+ '_c1_crop'],
                  view_name = "mock-crop-grid",
                  dataset = "./data/tomo"):
    
    """Add a grid view using the 'transformGrid' sourceTransform after applying the transforms of an already exisiting transformedSource inside a view.
    """
    
    # make sure that the table is not there, otherwise this creates issues
    table_path = f"./data/tomo/tables/{view_name}/default.tsv"
    if os.path.exists(table_path):
        os.remove(table_path)
    
    meta = mobie.metadata.read_dataset_metadata(dataset)

    
    def get_affine_and_crop(source_name,meta):
        
        orig_view = meta['views'][source_name]

        
        return orig_view['sourceTransforms']
    
    
    def get_orig_source_name(source_name,meta):
        
        orig_view = meta['views'][source_name]
        
        trafo1 = orig_view['sourceTransforms'][0]
        
        trafo0 = trafo1[list(trafo1.keys())[0]]
        
        return trafo0['sources']

    

    additional_source_transforms = [
        trafo for source_name in source_names for trafo in get_affine_and_crop(source_name,meta)
    ]    
    

    
    
    view = mobie.metadata.get_grid_view(
        "data/tomo",
        view_name,
        [get_orig_source_name(source_name,meta) for source_name in source_names],
        use_transform_grid=True,
        center_at_origin=True,
        additional_source_transforms=additional_source_transforms,
        # here, we need to specify the actual sources for the grid transform as a dictionary
        # we need to specify the name of the transformed source for the grid, i.e. <SOURCE_NAME>_crpped
        grid_sources=[[source_name] for source_name in source_names]
    )
    mobie.validation.validate_view_metadata(view)
    mobie.metadata.add_view_to_dataset(dataset, view_name, view, overwrite=True)


# add_mock_crop_grid()
# add_mock_crop_grid_with_source_name_after_trafo()
