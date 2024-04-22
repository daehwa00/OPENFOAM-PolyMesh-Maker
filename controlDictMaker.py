import numpy as np


def make_controlDict(airfoil_x, airfoil_y):
    # arifoil_x, y로 referece area, length 설정
    # airfoil_x, y는 0~1 사이의 값으로 정규화 되어 있음
    area = 0.5 * np.abs(
        np.dot(airfoil_x, np.roll(airfoil_y, 1))
        - np.dot(airfoil_y, np.roll(airfoil_x, 1))
    )

    controlDict = f"""
/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Version:  11
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
FoamFile
{{
    format      ascii;
    class       dictionary;
    location    "system";
    object      controlDict;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     foamRun;

solver          incompressibleFluid;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         500;

deltaT          1;

writeControl    timeStep;

writeInterval   50;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

functions 
{{
    forceCoeffs 
    {{
        type            forceCoeffs;
        functionObjectLibs ("libforces.so"); // 라이브러리 로드
        outputControl   timeStep;            // 출력 주기 설정
        outputInterval  1;                   // 매 시간 단계마다 결과 출력

        patches         ( "walls" );       // Patches to calculate forces
        pName           p;                   // 압력 필드 이름
        UName           U;                   // 속도 필드 이름
        rhoName         rhoInf;              // 유체 밀도(무차원화를 위함)
        log             true;                // 로그 파일에 결과 기록
        rhoInf          1.225;               // 유입 유체 밀도 (kg/m^3)
        CofR            (0.25 0 0);          // 회전 중심 (x y z)

        // Reference values for force coefficient calculations
        liftDir         (0 1 0);             // 양력 방향
        dragDir         (1 0 0);             // 항력 방향
        magUInf         25.75;                  // 유입 속도 (m/s)
        lRef            1;         // 참조 길이 (m)
        Aref            {area};       // 참조 면적 (m^2)
    }}
}}
"""
    with open("system/controlDict", "w") as f:
        f.write(controlDict)
