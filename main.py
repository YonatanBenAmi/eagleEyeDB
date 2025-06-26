from DAL.conection import AgentDAL


def main():
    agent_1 = AgentDAL()
    agent_1.create_aget("HG76G4", "Yonatan", "Rozzobski 9", "active", 34)

main()