
from mcpi.minecraft import Minecraft


class MattsMinecraft:

    playerpos = ''
    mc = ''
    standard_brick = 1
    tele_position = []

    def __init__ (self):
        print("minecraft class initiated")
        self.mc = Minecraft.create()

    def get_position(self):
        print("getting position")
        self.playerpos = self.mc.player.getPos()
        print("x: " + str(self.playerpos.x) + "y: " + str(self.playerpos.y) + "z: " + str(self.playerpos.z))

    def set_tele_position(self):
        self.get_position()
        self.tele_position = self.playerpos
        print("tele position set")

    def teleport(self,locindex):
        print("TELEPORTING!!!")
        self.get_position()
        x = self.playerpos.x - self.tele_position.x + self.playerpos.x
        y = self.playerpos.y - self.tele_position.y + self.playerpos.y
        z = self.playerpos.z - self.tele_position.z + self.playerpos.z
        self.mc.player.setPos(x, y, z)

    def build_a_brick(self, x, y, z):
        self.mc.setBlock(x, y, z, self.standard_brick)

    #zaway default to 1 so that you don't build the block on yourself
    def block_from_self(self):
	self.get_position()
	self.build_a_block(self.playerpos.x, self.playerpos.y, self.playerpos.z, 10.0,10.0,10.0)
	

    def build_a_block(self,x,y,z, width, height, depth):
        self.mc.setBlocks(x, y, z, x+width, y+height, z+depth, self.standard_brick)

    def building(self, width, height, depth):
        print("making a building")
        self.build_a_block(self.playerpos.x + 1, self.playerpos.y, self.playerpos.z + 1, width,height,depth)
        origbrick = self.standard_brick
        self.standard_brick = 0
        self.build_a_block(self.playerpos.x + 2, self.playerpos.y, self.playerpos.z, width-1,height-1,depth-1)
        self.standard_brick = origbrick

    # for each loop, increase height and increase xaway
    def stairs(self,dist):
        print("making some stairs")
        x = self.playerpos.x
        width = 1
        depth = 2
        height = 1
        xaway = 1
        zaway = 0
        truedist = x + dist
        while x < truedist:
            self.build_a_block(x,width,height,depth,xaway,zaway)
            xaway += 1
            height += 1
	    truedist += 1

    # build as you climb
    def ladder(self):
        print("building a ladder")

    def behind_as_you_walk():
        print("autoline")

    def ladder_as_you_climb():
        print("auto ladder")

    def print_variables(self):
        print("These are our variables: ")
        print("playerpos: " + self.playerpos)
        print("tele_position: " + self.tele_position)
        print("standard_brick: " + self.standard_brick)
        print("")

    def print_methods(self):
        print("These are the methods: \n\
        def get_position(self):\n\
        def set_tele_position(self):\n\
        def teleport(self,locindex):\n\
        def build_a_brick(self, x, y, z):\n\
        def build_a_block(self, width, height, depth, xaway, zaway=1):\n\
        def building(self, width, height, depth, xaway, zaway):\n\
        def stairs(self,dist):\n\
        ")

    def print_brick_options(self):
        print("These are the block options: \n\
            AIR                   0\n\
            STONE                 1\n\
            GRASS                 2\n\
            DIRT                  3\n\
            COBBLESTONE           4\n\
            WOOD_PLANKS           5\n\
            SAPLING               6\n\
            BEDROCK               7\n\
            WATER_FLOWING         8\n\
            WATER                 8\n\
            WATER_STATIONARY      9\n\
            LAVA_FLOWING         10\n\
            LAVA                 10\n\
            LAVA_STATIONARY      11\n\
            SAND                 12\n\
            GRAVEL               13\n\
            GOLD_ORE             14\n\
            IRON_ORE             15\n\
            COAL_ORE             16\n\
            WOOD                 17\n\
            LEAVES               18\n\
            GLASS                20\n\
            LAPIS_LAZULI_ORE     21\n\
            LAPIS_LAZULI_BLOCK   22\n\
            SANDSTONE            24\n\
            BED                  26\n\
            COBWEB               30\n\
            GRASS_TALL           31\n\
            WOOL                 35\n\
            FLOWER_YELLOW        37\n\
            FLOWER_CYAN          38\n\
            MUSHROOM_BROWN       39\n\
            MUSHROOM_RED         40\n\
            GOLD_BLOCK           41\n\
            IRON_BLOCK           42\n\
            STONE_SLAB_DOUBLE    43\n\
            STONE_SLAB           44\n\
            BRICK_BLOCK          45\n\
            TNT                  46\n\
            BOOKSHELF            47\n\
            MOSS_STONE           48\n\
            OBSIDIAN             49\n\
            TORCH                50\n\
            FIRE                 51\n\
            STAIRS_WOOD          53\n\
            CHEST                54\n\
            DIAMOND_ORE          56\n\
            DIAMOND_BLOCK        57\n\
            CRAFTING_TABLE       58\n\
            FARMLAND             60\n\
            FURNACE_INACTIVE     61\n\
            FURNACE_ACTIVE       62\n\
            DOOR_WOOD            64\n\
            LADDER               65\n\
            STAIRS_COBBLESTONE   67\n\
            DOOR_IRON            71\n\
            REDSTONE_ORE         73\n\
            SNOW                 78\n\
            ICE                  79\n\
            SNOW_BLOCK           80\n\
            CACTUS               81\n\
            CLAY                 82\n\
            SUGAR_CANE           83\n\
            FENCE                85\n\
            GLOWSTONE_BLOCK      89\n\
            BEDROCK_INVISIBLE    95\n\
            STONE_BRICK          98\n\
            GLASS_PANE          102\n\
            MELON               103\n\
            FENCE_GATE          107\n\
            GLOWING_OBSIDIAN    246\n\
            NETHER_REACTOR_CORE 247\n")

# WITH SETBLOCK, THESE ARE NOT NECESSARY
# all columns start at player z height
# def standard_column(self,height,x,z):
#     print("making a column")
#     brickpos = self.playerpos[1]
#     endpos = brickpos + height
#     while brickpos <= endpos:
#         self.build_a_brick(x,brickpos,z)
#         brickpos = brickpos + 1
#
# def standard_wall(self, x, z, direction, length, height):
#     print("making a wall")
#     if (direction = "z"):
#         zpos = z
#         zend = z + length
#         while zpos <= zend:
#             self.standard_column(height, x, zpos)
#             zpos = zpos + 1
#     if (direction = "x"):
#         xpos = x
#         xend = x + length
#         while xpos <= xend:
#             self.standard_column(height, xpos, z)
#             xpos = xpos + 1
