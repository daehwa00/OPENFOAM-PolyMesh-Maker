import argparse
import math

# 명령줄 인수 처리를 위한 Parser 설정
parser = argparse.ArgumentParser(
    description="Generate a blockMeshDict file for OpenFOAM with dynamic vertices."
)
parser.add_argument(
    "--distance_to_inlet",
    type=float,
    default=12,
    help="Distance to inlet (x chord length)",
)
parser.add_argument(
    "--distance_to_outlet",
    type=float,
    default=20,
    help="Distance to outlet (x chord length)",
)
parser.add_argument(
    "--angle_of_response", type=float, default=5, help="Angle of response (degree)"
)
parser.add_argument(
    "--depth_z_in_direction", type=float, default=0.3, help="Depth in Z direction"
)
parser.add_argument("--mesh_scale", type=float, default=1, help="Mesh scale")
parser.add_argument(
    "--expansion_ratio", type=float, default=1.2, help="Expansion ratio"
)
parser.add_argument(
    "--first_layer_thickness", type=float, default=0.005, help="First layer thickness"
)
parser.add_argument(
    "--boundary_layer_thickness",
    type=float,
    default=0.5,
    help="Boundary layer thickness",
)
parser.add_argument(
    "--max_cell_size_in_inlet", type=float, default=1, help="Max cell size in inlet"
)
parser.add_argument(
    "--max_cell_size_in_outlet", type=float, default=1, help="Max cell size in outlet"
)
parser.add_argument(
    "--max_cell_size_in_inlet_x_outlet",
    type=float,
    default=1,
    help="Max cell size in inlet x outlet",
)
parser.add_argument(
    "--seperating_point_position",
    type=float,
    default=0.4,
    help="Seperating point position",
)
parser.add_argument(
    "--cell_size_at_leading_edge",
    type=float,
    default=0.01,
    help="Cell size at leading edge",
)
parser.add_argument(
    "--cell_size_at_trailing_edge",
    type=float,
    default=0.03,
    help="Cell size at trailing edge",
)
parser.add_argument(
    "--cell_size_in_middle", type=float, default=0.035, help="Cell size in middle"
)

# 인수 파싱
args = parser.parse_args()


number_of_mesh_on_boundary_layer = n_10 = 17
inlet_expansion_ratio_1 = o_28 = (
    args.cell_size_at_trailing_edge / args.max_cell_size_in_inlet
)
inlet_expansion_ratio_2 = o_29 = 0.25
last_layer_thickness = (
    args.first_layer_thickness * args.expansion_ratio**number_of_mesh_on_boundary_layer
)
o_10 = args.expansion_ratio**number_of_mesh_on_boundary_layer
o_13 = args.max_cell_size_in_inlet / last_layer_thickness
o_16 = args.max_cell_size_in_outlet / args.cell_size_at_trailing_edge
number_of_mesh_out_of_boundary_layer = n_13 = 31
number_of_mesh_at_tail = n_16 = 74
number_of_mesh_in_leading = o_21 = 21
number_of_mesh_in_trailing = o_23 = 20
divide_point = o_20 = args.seperating_point_position
expansion_ratio_in_leading = o_22 = (
    args.cell_size_in_middle / args.cell_size_at_leading_edge
)
expansion_ratio_at_outlet = (
    args.max_cell_size_in_inlet_x_outlet
    * o_13
    / args.max_cell_size_in_outlet
    * (
        (number_of_mesh_out_of_boundary_layer + number_of_mesh_on_boundary_layer)
        / number_of_mesh_out_of_boundary_layer
    )
)
r_of_mesh_in_trailing = 20
expansion_ratio_in_trailing = o_24 = (
    args.cell_size_in_middle / args.cell_size_at_trailing_edge
)

h_11 = last_layer_thickness / args.distance_to_inlet * (o_13 - 1) + 1
i_11 = math.log(o_13) / math.log(h_11)
h_13 = args.cell_size_at_trailing_edge / args.distance_to_outlet * (o_16 - 1) + 1
i_13 = math.log(o_16) / math.log(h_13)
h_15 = (
    args.cell_size_at_leading_edge
    / args.seperating_point_position
    * (expansion_ratio_in_leading - 1)
) + 1

i_15 = math.log(expansion_ratio_in_leading) / math.log(h_15)
h_17 = (
    args.cell_size_at_trailing_edge
    / (1 - args.cell_size_in_middle)
    * (expansion_ratio_in_trailing - 1)
    + 1
)
i_17 = math.log(expansion_ratio_in_trailing) / math.log(h_17)

print(f"last_layer_thickness: {last_layer_thickness}")  # V
print(f"expansion_ratio_at_outlet: {expansion_ratio_at_outlet}")  # V

# Print initial arguments for verification
print(f"distance_to_inlet: {args.distance_to_inlet}")
print(f"distance_to_outlet: {args.distance_to_outlet}")
print(f"angle_of_response: {args.angle_of_response}")
print(f"depth_z_in_direction: {args.depth_z_in_direction}")
print(f"mesh_scale: {args.mesh_scale}")
print(f"expansion_ratio: {args.expansion_ratio}")
print(f"first_layer_thickness: {args.first_layer_thickness}")
print(f"boundary_layer_thickness: {args.boundary_layer_thickness}")
print(f"max_cell_size_in_inlet: {args.max_cell_size_in_inlet}")
print(f"max_cell_size_in_outlet: {args.max_cell_size_in_outlet}")
print(f"max_cell_size_in_inlet_x_outlet: {args.max_cell_size_in_inlet_x_outlet}")
print(f"seperating_point_position: {args.seperating_point_position}")
print(f"cell_size_at_leading_edge: {args.cell_size_at_leading_edge}")
print(f"cell_size_at_trailing_edge: {args.cell_size_at_trailing_edge}")
print(f"cell_size_in_middle: {args.cell_size_in_middle}")


print(f"first_layer_thickness: {args.first_layer_thickness}")
print(f"boundary_layer_thickness: {args.boundary_layer_thickness}")
print(f"max_cell_size_in_inlet: {args.max_cell_size_in_inlet}")
print(f"max_cell_size_in_outlet: {args.max_cell_size_in_outlet}")
print(f"max_cell_size_in_inlet_x_outlet: {args.max_cell_size_in_inlet_x_outlet}")
print(f"seperating_point_position: {args.seperating_point_position}")
print(f"cell_size_at_leading_edge: {args.cell_size_at_leading_edge}")
print(f"cell_size_at_trailing_edge: {args.cell_size_at_trailing_edge}")
print(f"cell_size_in_middle: {args.cell_size_in_middle}")
print(f"expansion_ratio_in_trailing: {expansion_ratio_in_trailing}")  # V

print(f"number_of_mesh_on_boundary_layer: {number_of_mesh_on_boundary_layer}")  # V
print(
    f"number_of_mesh_out_of_boundary_layer: {number_of_mesh_out_of_boundary_layer}"
)  # V
print(f"number_of_mesh_at_tail: {number_of_mesh_at_tail}")  # V
print(f"number_of_mesh_in_trailing: {number_of_mesh_in_trailing}")  # V
print(f"inlet_expansion_ratio_1: {inlet_expansion_ratio_1}")  # V
print(f"inlet_expansion_ratio_2: {inlet_expansion_ratio_2}")  # V

print(f"o_10: {o_10}")  # V
print(f"o_13: {o_13}")  # V
print(f"o_16: {o_16}")  # V
print(f"h_11: {h_11}")  # V
print(f"i_11: {i_11}")  # V
print(f"h_13: {h_13}")  # V
print(f"i_13: {i_13}")  # V
print(f"h_15: {h_15}")  # V
print(f"i_15: {i_15}")  # V
print(f"h_17: {h_17}")  # V
print(f"i_17: {i_17}")  # V


# 꼭짓점 위치 계산
inlet_x = 1
outlet_x = 1 + args.distance_to_outlet
inlet_negative_x = 1 - args.distance_to_inlet
calculated_vertex_y = math.sin(math.pi / 180 * args.angle_of_response) * (
    args.distance_to_outlet + 1
)


# blockMeshDict 파일 내용 작성
block_mesh_content = f"""/*--------------------------------*- C++ -*----------------------------------*\\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  5                                     |
|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\/     M anipulation  |                                                 |
\\*---------------------------------------------------------------------------*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

convertToMeters {args.mesh_scale};
gemetry
{{
}}
vertices
(
    (0 0 0) // 0
    ({inlet_x} 0 0) // 1
    ({inlet_x} {args.distance_to_inlet} 0) // 2
    ({inlet_negative_x} 0 0) // 3
    (0 0 {args.depth_z_in_direction}) // 4
    ({inlet_x} 0 {args.depth_z_in_direction}) // 5
    ({inlet_x} {args.distance_to_inlet} {args.depth_z_in_direction}) // 6
    ({inlet_negative_x} 0 {args.depth_z_in_direction}) // 7
    ({outlet_x} {calculated_vertex_y:.8f} 0) // 8
    ({outlet_x} {args.distance_to_inlet} 0) // 9
    ({outlet_x} {calculated_vertex_y:.8f} {args.depth_z_in_direction}) // 10
    ({outlet_x} {args.distance_to_inlet} {args.depth_z_in_direction}) // 11
    ({inlet_x} {-args.distance_to_inlet} 0) // {args.distance_to_inlet}
    ({inlet_x} {-args.distance_to_inlet} {args.depth_z_in_direction}) // 13
    ({outlet_x} {-args.distance_to_inlet} 0) // 14
    ({outlet_x} {-args.distance_to_inlet} {args.depth_z_in_direction}) // 15
    ({inlet_x} 0 0) // 16
    ({inlet_x} 0 {args.depth_z_in_direction}) // 17
);

blocks
(
    hex (0 1 2 3 4 5 6 7) ({o_21 + o_23} {n_10 + n_13} 1)  // block 1
    edgeGrading
    (
    // x-direction expansion ratio
    (
        ({o_20} {o_21/(o_21 + o_23)} {o_22})
        ({1 - o_20} {1-(o_21/(o_21 + o_23))} {1/o_24})
    )
    {o_28} {o_28}
    (
        ({o_20} {o_21/(o_21 + o_23)} {o_22})
        ({1 - o_20} {1-(o_21/(o_21 + o_23))} {1/o_24})
    )
    // y-direction expansion ratio
    (
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {o_13})
    )
    (
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {o_13})
    )
    (
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {o_13})
    )
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {o_13})
    )

    // z-direction expansion ratio
    1 1 1 1
    )
    
    hex (1 8 9 2 5 10 11 6) ({n_16} {n_10 + n_13} 1)    // block 2
    edgeGrading
    (
    // x-direction expansion ratio
    {o_16} {o_16} {o_16} {o_16}
    // y-direction expansion ratio
    (
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {o_13})
    )
    {expansion_ratio_at_outlet} {expansion_ratio_at_outlet}
    (
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {o_13})
    )

    // z-direction expansion ratio
    1 1 1 1
    ) 

    hex (3 12 16 0 7 13 17 4) ({o_21 + o_23} {n_10 + n_13} 1)    // block 3
    edgeGrading
    // x-direction expansion ratio
    {o_28}
    (
        ({o_20} {o_21/(o_21 + o_23)} {o_22})
        ({1 - o_20} {1-(o_21/(o_21 + o_23))} {1/o_24})
    )
    (
        ({o_20} {o_21/(o_21 + o_23)} {o_22})
        ({1 - o_20} {1-(o_21/(o_21 + o_23))} {1/o_24})
    )
    {o_28}
    // y-direction expansion ratio
    (
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {1/o_13})
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {1/o_10})
    )
    (
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {1/o_13})
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {1/o_10})
    )
    (
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {1/o_13})
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {1/o_10})
    )
    (
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {1/o_13})
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {1/o_10})
    )

    // z-direction expansion ratio
    1 1 1 1
    )

    hex (12 14 8 16 13 15 10 17) ({n_16} {n_10 + n_13} 1)    // block 4
    edgeGrading
    (
    // x-direction expansion ratio
    {o_16} {o_16} {o_16} {o_16}
    )
    // y-direction expansion ratio
    (
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {1/o_13})
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
    )
    {1/expansion_ratio_at_outlet} {1/expansion_ratio_at_outlet}
    (
        ({1 - args.boundary_layer_thickness/args.distance_to_inlet} {1-(n_10/(n_13 + n_10))} {1/o_13})
        ({args.boundary_layer_thickness/args.distance_to_inlet} {n_10/(n_13 + n_10)} {o_10})
    )
    // z-direction expansion ratio
    1 1 1 1
    )
);


edges
(
    arc 3 2 ({-args.distance_to_inlet*math.sin(math.pi/4)+1} {args.distance_to_inlet*math.cos(math.pi/4)} 0)
    arc 7 6 ({-args.distance_to_inlet*math.sin(math.pi/4)+1} {args.distance_to_inlet*math.cos(math.pi/4)} {args.depth_z_in_direction})

    spline 1 0
    (
        (0 0 0)
        (0 0 {args.depth_z_in_direction})
    )

    spline 5 4
    (
        ({inlet_x} 0 0)
        ({inlet_x} 0 {args.depth_z_in_direction})
    )

    arc 3 12 ({-args.distance_to_inlet*math.sin(math.pi/4)+1} {-args.distance_to_inlet*math.cos(math.pi/4)} 0)
    arc 7 13 ({-args.distance_to_inlet*math.sin(math.pi/4)+1} {-args.distance_to_inlet*math.cos(math.pi/4)} {args.depth_z_in_direction})

    spline 0 16
    (
        (0 0 0)
        ({inlet_x} 0 0)
    )

    spline 4 17
    (
        (0 0 {args.depth_z_in_direction})
        ({inlet_x} 0 {args.depth_z_in_direction})
    )
);

faces
(

);

faces
(

);

defaultPatch
{{
    name frontAndBack;
    type empty;
}}

boundary
(
inlet              // patch name
        {{
            type patch; 
            faces
            (
                (9 2 6 11)  
                (2 3 7 6  )  
                (3 12 13 7  )
                (12 15 14 13  )
            );
        }}

outlet              // patch name
        {{
            type patch;    
            faces
            (
                (8 9 10 11)  
                (15 8 10 14  ) 
            );
        }}

walls              // patch name
        {{
            type wall; 
            faces
            (
                (0 1 5 4)  
                (0 4 17 16  ) 
            );
        }}

interface1              // patch name
        {{
            type patch;   
            faces
            (
                (1 8 10 5)  
            );
        }}
interface2              // patch name
        {{
            type patch;    
            faces
            (
                (16 17 10 8)  
            );
        }}
);

 mergePatchPairs
(
    ( interface1 interface2 )
);

"""

# blockMeshDict 파일 생성
with open("blockMeshDict", "w") as f:
    f.write(block_mesh_content)
