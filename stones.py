# private static String winner(int n) {
#     String[] memory = new String[101];
#     Arrays.fill(memory, "");
#     return winner(n, memory);
# }
#
# private static String winner(int n, String[] memory){
#
#     if(n == 1){
#         return "Second";
#     }
#
#     if(2 <= n  && n <= 5){
#         return "First";
#     }
#
#     if(memory[n] == ""){
#         if(winner(n - 5, memory) == "First"
#                 && winner(n - 3, memory) == "First"
#                 && winner(n - 2, memory) == "First"){
#             memory[n] = "Second";
#         }
#         else{
#             memory[n] = "First";
#         }
#     }
#
#     return memory[n];
#
# }
