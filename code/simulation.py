# -*- coding: utf-8 -*-

# Imports
import random

import numpy as np

from helper import findOtherEdgeEnd, findConnection

def initializeEdgeCost(edge):
    
    # vertical edge
    if (edge._start._position[0] == edge._end._position[0]):
        edge._cost = abs(int(edge._start._position[1])) * abs(int(edge._start._position[1]))
        
    # horizontal edge
    elif (edge._start._position[1] == edge._end._position[1]):
        edge._cost = abs(int(edge._start._position[0])) * abs(int(edge._start._position[0]))
    
    return

"""_summary_
Initializes the conductivity (D_0) of all edges according to equation (1)
"""
def initializeConductivity(edge, viscosity):
    edge._conductivity = (np.pi * edge._radius ** 4) / (8 * viscosity)
    
    return


"""_summary_
Initializes the pressure vector (p^0) in all nodes according to equation (4). 
"""
def initializePressure(A, b, nodeList, terminalNodeList, initialFlow):
    
    for node in nodeList:
        
        if (node._sink == False and node._terminal == True):
            pressureVector = [0] * len(nodeList)
            
            for entry in nodeList:
                for neighbour in node._neighbours:
                    if (entry._id == node._id):
                        pressureVector[entry._id] = node._connections * node._initialPressure
                    elif (entry._id == neighbour._id):
                        pressureVector[entry._id] = -1 * node._initialPressure
            
            b.append((initialFlow * node._nodeEdgeList[0]._length) / node._nodeEdgeList[0]._conductivity)
            A.append(pressureVector)            
        
        elif (node._sink == True and node._terminal == True):
            pressureVector = [0] * len(nodeList)
            
            for entry in nodeList:
                for neighbour in node._neighbours:
                    if (entry._id == neighbour._id):
                        pressureVector[entry._id] = node._initialPressure
            
            b.append(((len(terminalNodeList) - 1) * initialFlow * node._nodeEdgeList[0]._length) / node._nodeEdgeList[0]._conductivity)
            A.append(pressureVector)       
        
        elif (node._sink == False and node._terminal == False):
            pressureVector = [0] * len(nodeList)
            
            for entry in nodeList:
                for neighbour in node._neighbours:
                    if (entry._id == node._id):
                        pressureVector[entry._id] = node._connections * node._initialPressure
                    elif (entry._id == neighbour._id):
                        pressureVector[entry._id] = -1 * node._initialPressure
            
            b.append(0)
            A.append(pressureVector)

    return


"""_summary_
Calculates the conductivity (D^t+1) throught each edge using equation (6)
"""
def calculateConductivity(currentNode, currentNeighbour, terminalNodeListLength, edgeList, sigma, rho, tau, viscosity):
        
    for edge in edgeList:
        
        if (currentNode._id == edge._start._id and currentNeighbour._id == edge._end._id) or (currentNeighbour._id == edge._start._id and currentNode._id == edge._end._id):
                pressureSum = 0
                for i in range(terminalNodeListLength):
                    pressureSum += edge._start._pressureVector[i] - edge._end._pressureVector[i]
                
                kappa = 1 + sigma * ((abs(pressureSum)) / edge._length) - rho * edge._cost
            
                edge._conductivity = edge._conductivity * kappa
                edge._radius = calculateRadius(edge, viscosity)

                
                # edge cutting
                if edge._conductivity < tau:
                    edgeList.remove(edge)
                    print("REMOVES! tau = " + str(tau))
                
        
    return


"""_summary_
Approximates the pressure change (p^t+1) for each node using equation (9)
"""
def calculatePressure(currentNode, terminalNodeList, initialFlow):
        
    for i in range(len(terminalNodeList)):
        if (currentNode._terminal == True and currentNode._terminalId != i):
            conductivitySum = 0
            conductivityPressureSum = 0
            
            for edge in currentNode._nodeEdgeList:
                conductivitySum += edge._conductivity
                conductivityPressureSum += edge._conductivity * findOtherEdgeEnd(currentNode, edge)._pressureVector[i]
                
            currentNode._pressureVector[i] = (initialFlow * 1 + conductivityPressureSum) / conductivitySum
            
        elif (currentNode._terminal == True and currentNode._terminalId == i):
            currentNode._pressureVector[i] = 0
            
        elif (currentNode._terminal == False):
            conductivitySum = 0
            conductivityPressureSum = 0
            
            for edge in currentNode._nodeEdgeList:
                conductivitySum += edge._conductivity
                conductivityPressureSum += edge._conductivity * findOtherEdgeEnd(currentNode, edge)._pressureVector[i]
                
            currentNode._pressureVector[i] = conductivityPressureSum / conductivitySum
        
    return


"""_summary_
Calculates radius of each edge, derived from equation (1)
"""
def calculateRadius(edge, viscosity):
    return ((edge._conductivity * 8 * viscosity) / np.pi) ** (1 / 4)


"""_summary_
Function is used to initialize the Physarium simulation by setting the initial conductivity and pressure
"""
def initializePhysarium(edgeList, nodeList, terminalNodeList, viscosity = 1.0, initialFlow = 10.0):
    
    for edge in edgeList:
        initializeConductivity(edge, viscosity)
    
    for node in terminalNodeList:
        A = list()
        b = list()
        
        node._sink = True
        initializeEdgeCost(edge)
        initializePressure(A, b, nodeList, terminalNodeList, initialFlow)
        
        node._sink = False

        A = np.array(A)
        b = np.array(b)
        x = np.linalg.solve(A, b)

        for i in range(len(nodeList)):
            nodeList[i]._pressureVector.append(x[i])

    return
    

"""_summary_
Function is used to calculate each time step in the simulation
"""
def physarumAlgorithm(nodeList, terminalNodeList, edgeList, viscosity = 1.0, initialFlow = 0.5, sigma = 0.00000375, rho = 0.0002, tau = 0.0004):
    random.shuffle(nodeList)
    random.shuffle(edgeList)
    
    for node in nodeList:
        for neighbour in node._neighbours:
            calculateConductivity(node, neighbour, len(terminalNodeList), edgeList, sigma, rho, tau, viscosity)
        calculatePressure(node, terminalNodeList, initialFlow)

    return