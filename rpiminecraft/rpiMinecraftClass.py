
from mcpi.minecraft import Minecraft


class MattsMinecraft:

    playerpos = []
    mc = ''
    standard_block = ""
    tele_position = []

    def __init__ (self):
        print("minecraft class initiated")
        self.mc = Minecraft.create()

    def get_position(self):
        print("getting position")
        self.playerpos = mc.player.getPos()
        print("x: " + self.pos[0] + "y: " + self.pos[1] + "z: " + self.pos[2])

    def set_tele_position(self):
        self.get_position()
        self.tele_position = self.playerpos
        print("tele position set")

    def teleport(self,locindex):
        print("TELEPORTING!!!")
        self.get_position()
        x = self.tele_position[0] - self.playerpos[0] + self.tele_position[0]
        y = self.tele_position[1] - self.playerpos[1] + self.tele_position[1]
        z = self.tele_position[2] - self.playerpos[2] + self.tele_position[2]
        self.mc.player.setPos(x, y, z)

    def build_a_brick(self, x, y, z):
        self.mc.setBlock(x, y, z, self.standard_block)

    # all columns start at player z height
    def standard_column(self,height,x,z):
        print("making a column")
        brickpos = self.playerpos[1]
        endpos = brickpos + height
        while brickpos <= endpos:
            self.build_a_brick(x,brickpos,z)
            brickpos = brickpos + 1

    def standard_wall(self, x, z, direction, length, height):
        print("making a wall")
        if (direction = "z"):
            zpos = z
            zend = z + length
            while zpos <= zend:
                self.standard_column(height, x, zpos)
                zpos = zpos + 1
        if (direction = "x"):
            xpos = x
            xend = x + length
            while xpos <= xend:
                self.standard_column(height, xpos, z)
                xpos = xpos + 1

    def standard_roof(self):
        print("making a roof")

    def standard_tunnel(self):
        print("making a tunnel")

    def standard_building(self):
        print("making a building")

    def standard_stairs(self):
        print("making some stairs")

    def standard_ladder(self):
        print("building a ladder")

    def print_variables(self):
        print("These are our variables: ")
        print("playerpos: " + self.playerpos)
        print("tele_position: " + self.tele_position)
        print("standard_block: " + self.standard_block)
        print("")

    def print_methods(self):
        print("These are the methods: \n\
        def get_position(self):\n\
        def set_tele_position(self):\n\
        def teleport(self,locindex):\n\
        def build_a_brick(self, x, y, z):\n\
        def standard_column(self,height,x,z):\n\
        def standard_wall(self, x, z, direction, length, height):\n\
        ")

    def print_block_options(self):
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
            NETHER_REACTOR_CORE 247\n\")
