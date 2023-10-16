def solution(text):
    text_list = text.split()
    print(text_list)
    word_count = 0
    word_list = []
    answer_list = []
    answer = ""

    for i in range(1, len(text_list)+1):
        if i == len(text_list):
            break
        # TODO : 정렬 &
        if ("[") in text_list[i-1]:
            print(list(text_list[i-1]))
            print(str(text_list[i-1]).index("["))
            replace_text = text_list[i-1].replace("[", "")

            if replace_text.replace(",", "") not in str(word_list):
                word_count += 1
                word_list.append("["+str(word_count)+"] " + replace_text.replace(",", ""))
                answer_list.append("["+str(word_count)+", ")
            else:
                answer_list.append("["+str(word_count)+", ")
            if text_list[i] not in str(word_list):
                word_count += 1
                word_list.append("["+str(word_count)+"] " + text_list[i].replace("]", ""))
                answer_list.append(str(word_count)+"] ")
            else:
                answer_list.append(str(word_count)+"] ")
        if ("[") not in text_list[i-1] and ("]") not in text_list[i-1]:
            answer_list.append(text_list[i-1]+" ")
    print(word_list)
    for i in answer_list:
        answer += i
    print(answer)

    return answer

print(solution("Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.[ some_paper_a, some_paper_b ] We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions.[ some_book_a, some_paper_a ] We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. [ some_book_b ]"))