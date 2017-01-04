def simulate(Agentset, BF, years):
    for y in range(years):
        for agent in Agentset:
            agent.Age += 1
            if not agent.Auto_Renew:
                if agent.Agent_Breed == "Breed_C":
                    if agent.Affinity < (agent.Social_Grade * agent.Attribute_Brand):
                        """C -> NC : Breed_C Lost"""
                        agent.Agent_Breed = "Breed_NC"
                        agent.changetimes += 1
                        # agent.Breed_Last_Status = agent.Breed_Actual_Status
                        # agent.Breed_Actual_Status = "Lost"

                elif agent.Agent_Breed == "Breed_NC":
                    if agent.Affinity < (agent.Social_Grade * agent.Attribute_Brand * BF):
                        agent.Agent_Breed = "Breed_C"
                        agent.changetimes += 1
                        # agent.Breed_Last_Status = agent.Breed_Actual_Status
                        # if agent.Breed_Last_Status == "Lost":
                        #     agent.Breed_Actual_Status = "Regained"
                        # else:
                        #     agent.Breed_Actual_Status = "Gained"

        for agent in Agentset:
            if not agent.Auto_Renew:
                if agent.Agent_Breed == "Breed_C":
                    if agent.changetimes % 2 == 0 and agent.changetimes <> 0:
                        agent.Breed_Status = "Regained"
                    elif agent.changetimes % 2 <> 0:
                        agent.Breed_Status = "Lost"

                elif agent.Agent_Breed == "Breed_NC":
                    if agent.changetimes % 2 <> 0:
                        agent.Breed_Status = "Gained"

def statistic(Agentset):
    nbAgent = int(len(Agentset))
    nbBreed_C = 0
    nbBreed_NC = 0
    nbLost = 0
    nbGained = 0
    nbRegained = 0
    nbUnaltered = 0
    for agent in Agentset:
        if agent.Agent_Breed == "Breed_C":
            nbBreed_C += 1
        elif agent.Agent_Breed == "Breed_NC":
            nbBreed_NC += 1
        if agent.Breed_Status == "Lost":
            nbLost += 1
        elif agent.Breed_Status == "Gained":
            nbGained += 1
        elif agent.Breed_Status == "Regained":
            nbRegained += 1
    nbUnaltered = len(Agentset)-(nbLost+nbGained+nbRegained)
    count = [nbAgent, nbBreed_C ,nbBreed_NC, nbLost, nbGained, nbRegained,nbUnaltered]
    return count
