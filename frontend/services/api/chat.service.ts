import { apiFetch } from "./client"

type ChatResponse = {
  answer?: string
  final_response?: string
  response?: string
}

export async function sendMessage(
  message: string
): Promise<ChatResponse> {
  return apiFetch("/chat", {
    method: "POST",
    body: JSON.stringify({
      message
    })
  })
}
