num_of_streams=int(input())

streams=[int(input()) for flow in range(num_of_streams)]

while True:
    split_or_join=int(input())

    if (split_or_join==77):
        break

    if (split_or_join==99):
        split_stream=int(input())-1
        percent=int(input())

        flow=streams[split_stream]
        streams[split_stream]*=(percent/100)

        first_half=streams[:split_stream+1]
        first_half.append(flow-streams[split_stream])
        second_half=streams[split_stream+1:]

        streams=first_half+second_half

    elif (split_or_join==88):
        join_stream=int(input())-1

        streams[join_stream]+=streams[join_stream+1]

        streams=streams[:join_stream+1]+streams[join_stream+2:]


streams=[str(int(round(flow,0))) for flow in streams]

print(' '.join(streams))

        
        
