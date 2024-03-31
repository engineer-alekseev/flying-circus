export type iModelSelectValue<t = string | boolean | number | null> = {
    title: string
    value: t
    bg?: string
    disabled?: boolean
    svg?: string
    isError?: boolean // если шлем, то покажет красным при выборе
    isLoading?: boolean // одно значение с загрузкой, то покажет загрузку
  }
  
  export type iModelOptions = Record<string, iModelOption>
  
  export interface iModelOption {
    type?: "text" | "number" | "password"
    default_value?: string | number | boolean
    label?: string
    hint?: string
    values?: iModelSelectValue[]
    error?: string
    validate?: iModelOptionValidate
  }
  
  export interface iModelOptionValidate {
    minLength?: number
    maxLength?: number
    required?: boolean | iModelRequiredFunction
    custom?: {
        rule: (value: string | number | boolean, model: iModelOptions) => boolean | Promise<boolean>
        text: string
    }[]
  }
  
  type iModelRequiredFunction = (model: iModelOptions, entity: Record<string, any>) => boolean
  
  export type iModelEntity = Record<string, any>
  
  export type iModelEntityErrors = Record<string, string>
  