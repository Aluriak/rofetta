product("d","R2").
dreaction("R_importS2").
reversible("R_importS2").
reactant("c","R5").
reactant("f","R_exportF").
product("S1","R_importS1").
dreaction("R2").
product("S2","R_importS2").
dreaction("R1").
reactant("S3","R1").
reactant("b","R0").
dreaction("R0").
dreaction("R4").
reactant("S2","R2").
reactant("e","R4").
dreaction("R_importS1").
product("S3","R0").
reactant("c","R2").
dreaction("R5").
product("f","R5").
dreaction("R_exportF").
reversible("R_importS1").
product("c","R4").
reactant("a","R5").
reactant("d","R3").
product("b","R1").
product("e","R3").
dreaction("R3").

% define the relations between reactants and products of same reaction.
rel(R,P):- reactant(R,F) ; product(F,P).
