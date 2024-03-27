import pygame, json
from pygame.locals import *

def main():
    pygame.init()

    BLACK = (0, 0, 0)
    GRAY = (127, 127, 127)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)

    screen = pygame.display.set_mode([300,450])
    pygame.display.set_caption('Clicking Game')
    background = BLACK
    framerate = 60
    font = pygame.font.SysFont('aptos.ttf', 20)
    banana_font = pygame.font.SysFont('aptos.ttf', 80)
    buy_font = pygame.font.SysFont('aptos.ttf', 12)
    timer = pygame.time.Clock()

    # game variables 
    bananas_per_second = 0
    
    clicker_production = 0
    field_production = 0
    mine_production = 0
    factory_production = 0
    bank_production = 0
    time_production = 0

    with open('mydata.json', 'r') as fileref: 
        data = json.load(fileref)
    

    clicker_base_cost = 2
    field_base_cost = 5
    mine_base_cost = 100 
    factory_base_cost = 500 
    bank_base_cost = 1500
    time_shipment_base_cost = 10000

    clicker_next_cost = int(clicker_base_cost * (1.08 ** data['clickers_owned']))
    field_next_cost = int(field_base_cost * (1.20 ** data['fields_owned']))
    mine_next_cost = int(mine_base_cost * (1.43 ** data['mines_owned'])) 
    factory_next_cost = int(factory_base_cost * (1.35 ** data['factories_owned']))
    bank_next_cost = int(bank_base_cost * (1.75 ** data['banks_owned']))
    time_shipment_next_cost = int(time_shipment_base_cost * (1.05 ** data['time_shipments_owned']))

    clicker_production = data['clickers_owned'] * 2



    def draw_rectangle(color, x_coord, y_coord):
        return pygame.draw.rect(screen, color, [x_coord, y_coord, 18, 18], 1)

    running = True

    while running:
        timer.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.ACTIVEEVENT:
                pygame.time.set_timer(pygame.ACTIVEEVENT, 1000)
                bananas_per_second = clicker_production + field_production + mine_production + factory_production + bank_production + time_production
                data["bananas"] += bananas_per_second
            if event.type == pygame.MOUSEBUTTONDOWN:
                if banana_rect.collidepoint(event.pos):
                    data["bananas"] += 1
                if clicker_button.collidepoint(event.pos):
                    if data["bananas"] - clicker_next_cost < 0:
                        data['clickers_owned'] += 0
                    else:
                        data["bananas"] -= clicker_next_cost
                        data['clickers_owned'] += 1
                    clicker_next_cost = int(clicker_base_cost * (1.30 ** data['clickers_owned']))
                if field_button.collidepoint(event.pos):
                    if data["bananas"] - field_next_cost < 0:
                        data['fields_owned'] += 0
                    else:
                        data["bananas"] -= field_next_cost
                        data['fields_owned'] += 1
                    field_next_cost = int(field_base_cost * (1.30 ** data['fields_owned']))
                    field_production = data['fields_owned'] * 5
                if mine_button.collidepoint(event.pos):
                    if data["bananas"] - mine_next_cost < 0:
                        data['mines_owned'] += 0
                    else:
                        data["bananas"] -= mine_next_cost
                        data['mines_owned'] += 1
                    mine_next_cost = int(mine_base_cost * (1.30 ** data['mines_owned']))
                    mine_production = data['mines_owned'] * 20
                if factory_button.collidepoint(event.pos):
                    if data["bananas"] - factory_next_cost < 0:
                        data['factories_owned'] += 0
                    else:
                        data["bananas"] -= factory_next_cost
                        data['factories_owned'] += 1
                    factory_next_cost = int(factory_base_cost * (1.30 ** data['factories_owned']))
                    factory_production = data['factories_owned'] * 40
                if bank_button.collidepoint(event.pos):
                    if data["bananas"] - bank_next_cost < 0:
                        data['banks_owned'] += 0
                    else:
                        data["bananas"] -= bank_next_cost
                        data['banks_owned'] += 1
                    bank_next_cost = int(bank_base_cost * (1.30 ** data['banks_owned']))
                    bank_production = data['banks_owned'] * 100
                if time_button.collidepoint(event.pos):
                    if data["bananas"] - time_shipment_next_cost < 0:
                        data['time_shipments_owned'] += 0
                    else:
                        data["bananas"] -= time_shipment_next_cost
                        data['time_shipments_owned'] += 1
                    time_shipment_next_cost = int(time_shipment_base_cost * (1.30 ** data['time_shipments_owned']))
                    time_production = data['time_shipments_owned'] * 200
            


        screen.fill(background)

        bananas_per_second_text = font.render(f"bananas per second: {str(bananas_per_second)}", True, WHITE)
        screen.blit(bananas_per_second_text, [0, 0])

        if data["bananas"] < 1000000:
            banana_holder = data["bananas"]
            banana_text = banana_font.render(str(banana_holder), True, WHITE)
        if data["bananas"] > 1000000 and data["bananas"] < 1000000000:
            banana_holder = str(data["bananas"])[:2] + "." + str(data["bananas"])[2:5] + "mil"
            banana_text = banana_font.render(str(banana_holder), True, WHITE)
        if data["bananas"] > 1000000000 and data["bananas"] < 1000000000000:
            banana_holder = str(data["bananas"])[:2] + "." + str(data["bananas"])[3:5] + "bil"
            banana_text = banana_font.render(str(banana_holder), True, WHITE)

        
        banana_rect = banana_text.get_rect(topleft=[0,150])
        screen.blit(banana_text, banana_rect)

        # Buy object
        buy_text = buy_font.render("Buy", True, WHITE)
        
        # clicker box
            # "Have: " text 
        clickers_owned_text = font.render(f"clickers: {str(data['clickers_owned'])}", True, MAGENTA)
        screen.blit(clickers_owned_text, [2, 350])
            # "Cost: " text
        clicker_cost_text = font.render(f"${str(clicker_next_cost)}", True, GREEN)
        screen.blit(clicker_cost_text, [2, 375])
            # "Buy" text
        screen.blit(buy_text, [50,375])
            #  Button 
        clicker_button = draw_rectangle(WHITE, 50, 370)


        # field box
            # "Have: " text
        fields_owned_text = font.render(f"fields: {str(data['fields_owned'])}", True, MAGENTA)
        screen.blit(fields_owned_text, [2, 400])
            # "Cost: " text
        field_next_cost_text = font.render(f"${str(field_next_cost)}", True, GREEN)
        screen.blit(field_next_cost_text, [2, 425])
            # "Buy" text 
        screen.blit(buy_text, [50,425])
            #  Button
        field_button = draw_rectangle(WHITE, 50, 420)

        # mine box
            # "mines: " text
        mines_owned_text = font.render(f"mines: {str(data['mines_owned'])}", True, MAGENTA)
        screen.blit(mines_owned_text, [95, 350])
            # "$" text
        mine_next_cost_text = font.render(f"${str(mine_next_cost)}", True, GREEN)
        screen.blit(mine_next_cost_text, [95, 375])
            # "Buy" text
        screen.blit(buy_text, [145, 375])
            #  Button
        mine_button = draw_rectangle(WHITE, 145, 370)

        # factory box
            # "factories: " text
        factories_owned_text = font.render(f"factories: {str(data['factories_owned'])}", True, MAGENTA)
        screen.blit(factories_owned_text, [95, 400])
            # "$" text
        factory_next_cost_text = font.render(f"${str(factory_next_cost)}", True, GREEN)
        screen.blit(factory_next_cost_text, [95, 425])
            # "Buy" text
        screen.blit(buy_text, [145, 425])
            #  Button
        factory_button = draw_rectangle(WHITE, 145, 420)

        # bank box
            # "banks: " text
        banks_owned_text = font.render(f"banks: {str(data['banks_owned'])}", True, MAGENTA)
        screen.blit(banks_owned_text, [180,350])
            # "$" text
        bank_next_cost_text = font.render(f"${str(bank_next_cost)}", True, GREEN)
        screen.blit(bank_next_cost_text, [180, 375])
            # "Buy" text
        screen.blit(buy_text, [230, 375])
            #  Button
        bank_button = draw_rectangle(WHITE, 230, 370)

        # time box
            # "time boxes: " text
        time_shipments_owned_text = font.render(f"time boxes: {str(data['time_shipments_owned'])}", True, MAGENTA)
        screen.blit(time_shipments_owned_text, [180, 400])
            # "$" text
        time_shipment_next_cost_text = font.render(f"${str(time_shipment_next_cost)}", True, GREEN)
        screen.blit(time_shipment_next_cost_text, [180, 425])
            # "Buy" text
        screen.blit(buy_text, [230, 425])
            #  Button
        time_button = draw_rectangle(WHITE, 230, 420)

    
        with open("mydata.json", "w") as fileref:
            json.dump(data, fileref)
        

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()