def get_values(*names):
    import json
    _all_values = json.loads("""{"p300_mount":"left","poolVolR": 600, "poolVolC": 800, "num_samp": 48,"numPoolsR": 6, "numPoolsC": 8,"pooledTotal": 14}""")
    return [_all_values[n] for n in names]
    
# flake8: noqa

import math 

metadata = {
    'protocolName': '2D Pooling',
    'author': 'Hermela Solomon <hsolomon@sgbio.com>',
    'source': 'Custom Protocol',
    'apiLevel': '2.13'
}


def run(protocol):
    
    [p300_mount, poolVol_r, poolVol_c, num_samp, numPools_r, numPools_c, pooledTotal] = get_values(  # noqa: F821
     'p300_mount', 'poolVolR', 'poolVolC', 'num_samp', 'numPoolsR', "numPoolsC", "pooledTotal")

    #labware
    #we don't have the API name for the custom labware or the json file - contact Opentron about this
   # h

    #tuberack = [protocol.load_labware('opentrons_24_tuberack_2000ul', slot) for slot in [6]]
    
    tip300 =[protocol.load_labware('opentrons_96_tiprack_300ul', s) for s in [10, 11]]

    #pipettes
    p300 = protocol.load_instrument(
        'p300_single_gen2', p300_mount, tip_racks=[tip300])
   
    #p1000.flow_rate.aspirate = 300
    #p1000.flow_rate.dispense = 300

    poolRack = [protocol.load_labware('opentrons_24_tuberack_2000ul', s) for s in [9]]

    #visbys = [
       # protocol.load_labware(
            #'visby', s) for s in [10, 11, 7, 8, 9, 4][:numVisbys]]

    poolRack = protocol.load_labware('opentrons_24_tuberack_2000ul', '9')


    protocol.comment('\n---------------POOLING BY ROW VARIABLES----------------\n\n')


    pool_r = poolVolR/numPoolsR
    pooledSamps_r = [
        poolRack[w] for w in ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'[:]]
                              
    rowSamps = [protocol.load_labware('custom_pooling_tuberack_2000ul', s) for s in [1, 2, 4, 5][:numPools].rows()

    protocol.comment('\n---------------POOLING BY COLUMN VARIABLES----------------\n\n')          

    pool_c = poolVolC/numPoolsC
    pooledSamps_c = [
        poolRack[w] for w in ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'C1', 'C2']
                                         
    colSamps = [protocol.load_labware('custom_pooling_tuberack_2000ul', s) for s in [1, 2, 4, 5][:numPools].columns()


    sample1

    sample2

    sample3

    sample4


    



    

    protocol.comment(f'\nPooling Samples: {pvol}uL-->{poolVol}uL\n')


    protocol.comment('\n---------------POOLING BY ROW----------------\n\n')
    
    for samps, pool in zip(rowSamps, pooledSamps):
        for samp in samps[:numPools]:
            p1000.pick_up_tip()



    


    protocol.comment('\n---------------POOLING BY COLUMN----------------\n\n')           

     for samps, pool in zip(colSamps, pooledSamps):
        for samp in samps[:numPools]:
            p1000.pick_up_tip()




                
    if numVisbys > 3:
        iSamps += protocol.load_labware(
            'basisdx_15_tuberack_12000ul', '3').rows()
    gap = 50


   

    protocol.comment(f'\nPooling Samples: {pvol}uL-->{poolVol}uL\n')
    for samps, pool in zip(iSamps, pooledSamps):
        for samp in samps[:numPools]:
            p1000.pick_up_tip()
            p1000.aspirate(100, samp.top())
            p1000.aspirate(pvol, samp.bottom(10))
            protocol.delay(seconds=1)
            p1000.move_to(samp.top())
            p1000.air_gap(gap)
            p1000.dispense(100+pvol+gap, pool.top(-30))
            p1000.drop_tip(home_after=False)

    for idx, (visby, pool) in enumerate(zip(visbys, pooledSamps)):
        protocol.comment(f'\nTransferring {poolVol}uL to Visby {idx+1}\n')
        p1000.pick_up_tip()
        p1000.mix(1, poolVol*.9, pool.bottom(38))

        p1000.aspirate(poolVol, pool.bottom(38))
        protocol.delay(seconds=1)
        p1000.move_to(pool.top())
        p1000.air_gap(gap)
        p1000.dispense(poolVol+gap+20, visby['A1'].bottom(10))
        protocol.delay(seconds=1)
        p1000.drop_tip(home_after=False)

    protocol.comment('\nProtocol complete!')
