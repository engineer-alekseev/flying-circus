import {iModelEntity, iModelEntityErrors, iModelOptions, iModelOptionValidate} from "../models/form_data"

export const validateModel = async (validateOptions: iModelOptions, entity: iModelEntity): Promise<{ model: iModelOptions, errors: iModelEntityErrors, status: boolean }> => {
    const keys = Object.keys(validateOptions)
    let has_errors = false

    let errors: iModelEntityErrors = {}

    for (const field_key of keys) {
        if (!(field_key in entity)) continue;

        const value = entity[field_key]

        let field_errors = []

        if (!validateOptions[field_key].validate || typeof validateOptions[field_key].validate !== 'object') continue

        const validate = validateOptions[field_key].validate as iModelOptionValidate
        // alert(validate.minLength)
        // min and max length

        if (typeof value === 'string' && (validate.minLength && value.length < validate.minLength) || (validate.maxLength && value.length < validate.maxLength)) {
        // if (typeof value === 'string' && (validate.minLength && value.length < validate.minLength) || (validate.maxLength && value.length < validate.maxLength)) {
        // if (typeof value === 'string' && (validate.minLength && value.length < validate.minLength) || (validate.maxLength && value.length < validate.maxLength)) {

          field_errors.push(`Значение должно быть от ${ validate.minLength } до ${ validate.maxLength } символов`)
        }

        // required
        if (validate.required) {
            let is_required = false

            if (typeof validate.required === "function") {
                is_required = validate.required(validateOptions, entity)
            } else {
                is_required = validate.required
            }

            if (is_required) {
                let required_err: boolean

                if (typeof value === 'boolean') {
                    required_err = !value
                } else if (typeof value === 'string') {
                    required_err = value.length === 0
                } else if (typeof value === 'number') {
                    required_err = value === 0
                } else {
                    required_err = value === null
                }

                if (required_err) {
                    field_errors.push("Поле обязательно")
                }
            }

            if (Array.isArray(validate.custom)) {
                for (let rule of validate.custom) {
                    // @ts-ignore
                    let res = await rule.rule(value, model)

                    if (!res) {
                        field_errors.push(rule.text)
                        break;
                    }
                }
            }

            errors[field_key] = field_errors.length > 0 ? field_errors[0] : ""

            // validateOptions[field_key]["error"] = errors[0]

            if (!has_errors) {
                has_errors = field_errors.length > 0
            }
        }
    }

    return {
        model: validateOptions,
        errors,
        status: !has_errors
    }
}

export function clearEntity (entity: iModelEntity, modelOptions: iModelOptions): iModelEntity {
    const keys = Object.keys(entity)

    for (let key of keys) {
        if (key in modelOptions && modelOptions[key].default_value) {
            entity[key] = modelOptions[key].default_value
        } else {
            if (typeof entity[key] === "boolean") {
                entity[key] = false
            } else if (typeof entity[key] === "number") {
                entity[key] = null
            } else if (Array.isArray(entity[key])) {
                entity[key] = []
            } else if (typeof entity[key] === 'string') {
                entity[key] = ""
            }
        }
    }

    return entity
}

export function setEntitySafe <Type = iModelEntity>(entity: Type, data: object): Type {
    let res: Type = {
        ...entity
    }
    // @ts-ignore
    Object.keys(entity).map((key: string) => {
        if (key in data) {
            // @ts-ignore
            res[key] = data[key]
        }
    })
    return res
}
